import pickle
import numpy as np
import scipy.sparse
import pandas as pd
from pathlib import Path

def LoadDataSetWithFeature(data_path : Path, feature_list : list) -> pd.DataFrame:
    df = pd.read_csv(data_path)
    df=df[feature_list]
    return df

def SaveObjects(path : Path, object):
    pickle.dump(object, open(path,'wb'))

def SaveDataFrame(dataframe:pd.DataFrame, save_path):
    dataframe.to_csv(save_path,index=False)

def SaveMatrixAsCsv(data, path: Path):
    # Check if the data is a sparse matrix and convert it to a dense array if so
    if scipy.sparse.issparse(data):
        data = data.toarray()
    # Save the dense array to a CSV file
    np.savetxt(path, data, delimiter=',', fmt='%f')

def LoadDataSet(data_path : Path) -> pd.DataFrame:
    df = pd.read_csv(data_path)
    return df

def LoadNumpyMetrix(path : Path) -> np.ndarray:
    return np.genfromtxt(path, delimiter=',')

