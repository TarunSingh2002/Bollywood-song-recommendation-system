import sys
from pathlib import Path
from logger import logging
from base import LoadNumpyMetrix, SaveObjects
from sklearn.metrics.pairwise import cosine_similarity

def main():
    current_path = Path(__file__)

    root_path = current_path.parent.parent

    data_path = root_path / sys.argv[1]

    save_model_path = root_path / 'models'
    save_model_path.mkdir(exist_ok=True)

    logging.info("Getting the processed-data")

    data = LoadNumpyMetrix(data_path)

    logging.info("Getting the cosine similarity")

    similarity=cosine_similarity(data)

    logging.info("Saving the cosine similarity metrix as similarity.plk")

    SaveObjects(path = save_model_path / 'similarity.pkl' , object= similarity)

    logging.info("Modeling part completed")

if __name__ == "__main__":
    main()