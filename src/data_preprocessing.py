import sys
import numpy as np
import pandas as pd
from pathlib import Path
from yaml import safe_load
from logger import logging
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from base import LoadDataSetWithFeature, SaveObjects, SaveMatrixAsCsv

class CategoryGrouper(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=44, new_category='other'):
        self.threshold = threshold
        self.new_category = new_category
        
    def fit(self, X, y=None):
        # Ensure X is a DataFrame
        if isinstance(X, pd.Series):
            X = X.to_frame()
        elif not isinstance(X, pd.DataFrame):
            raise TypeError("Input X should be a pandas DataFrame or Series.")
        
        # Determine the column name
        self.column = X.columns[0]  # Assumes the first column is the target
        # Calculate the frequency of each category
        freq = X[self.column].value_counts()
        # Identify categories to keep
        self.categories_to_keep_ = freq[freq >= self.threshold].index
        return self
    
    def transform(self, X):
        # Ensure X is a DataFrame
        if isinstance(X, pd.Series):
            X = X.to_frame()
        elif not isinstance(X, pd.DataFrame):
            raise TypeError("Input X should be a pandas DataFrame or Series.")
        
        # Apply the transformation
        X = X.copy()  # To avoid modifying the original dataframe
        X[self.column] = np.where(X[self.column].isin(self.categories_to_keep_), 
                                  X[self.column], self.new_category)
        return X

def make_pipeline() -> Pipeline :

    logging.info("Making a pipeline")

    pipe = Pipeline(
        [
            ('transformation3',CategoryGrouper()),
            ('transformation4',OneHotEncoder())
        ]
    )
    return pipe

def make_transformer() -> tuple[ColumnTransformer, list]:

    with open('params.yaml') as f:
        params = safe_load(f)

    feature_list = params['data_preprocessing']['feature']

    pipe = make_pipeline()

    simple_imputer_strategy = params['data_preprocessing']['SimpleImputer']['strategy']
    simple_imputer_fill_value = params['data_preprocessing']['SimpleImputer']['fill_value']
    simple_imputer_feature_list = params['data_preprocessing']['SimpleImputer']['feature']
    min_max_scaler_feature_list = params['data_preprocessing']['MinMaxScaler']['feature']
    pipeline_feature_list = params['data_preprocessing']['pipe']['feature']

    logging.info("Making a column transformer")

    transform = ColumnTransformer(transformers=[
        ('transformation1',SimpleImputer(strategy=simple_imputer_strategy , fill_value=simple_imputer_fill_value),simple_imputer_feature_list),
        ('transformation2',MinMaxScaler(),[min_max_scaler_feature_list]), 
        ('pipe',pipe,[pipeline_feature_list])
    ], remainder='passthrough')

    return transform, feature_list

def main():

    current_path = Path(__file__)

    root_path = current_path.parent.parent

    training_data_path = root_path / sys.argv[1]

    logging.info("Getting the pre-processor and list of all features")

    transformer, fetaure_list = make_transformer()

    logging.info("Loading the data frame")

    data_frame = LoadDataSetWithFeature(training_data_path,fetaure_list)

    logging.info("Appling the transformation")

    data = transformer.fit_transform(data_frame)

    logging.info(f"Data after transformation: \n{data}")

    save_transformers_path = root_path / 'preprocessor' 
    save_transformers_path.mkdir(exist_ok=True)
    
    save_data_path = root_path / 'data' / 'processed'
    save_data_path.mkdir(exist_ok=True)

    logging.info("Saving the preprocessor")

    SaveObjects(path=save_transformers_path / 'preprocessor.pkl', object=transformer)

    logging.info("Saving the proecessed data")

    SaveMatrixAsCsv(data=data, path=save_data_path / 'data.csv')

    logging.info("Data_processing part completed")

if __name__ == "__main__":
    main()








































