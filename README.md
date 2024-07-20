Project Organization
------------

    ├── LICENSE
    │
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── preprocessor       <- The preprocessor model.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── base.py        <- Scripts that contain most using functions
    │   │   
    │   ├── logger.py       <- Scripts to log the steps
    │   │   
    │   ├── data_preprocessing.py  <- Scripts for data preprocessing.
    │   │   
    │   └── model_training.py      <- Scripts to train models.
    │
    ├── static
    │   ├── css            <- The folder containing css related files.
    │   │   ├── style.css  <- The file containing css related clsses.
    │   │
    │   └── images         <- The folder images required for the app.
    │
    ├── templates          <- The folder conatin app html design.
    │    ├── index.html    <- The file conatin app html design.
    │
    ├── .gitignore         <- gitignore file.
    │     
    └── app.py             <- Flask app.

