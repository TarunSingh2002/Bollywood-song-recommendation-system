# Bollywood Song Recommendation System

Welcome to the Bollywood Song Recommendation System! This project uses machine learning to recommend Bollywood songs based on user preferences.

![Project Image 1](![lp0b66aa4h execute-api us-east-1 amazonaws com_Prod_ (1)](https://github.com/user-attachments/assets/6699c350-42ed-41b6-8cb4-e4b63edbfb69))

![Project Image 2](![lp0b66aa4h execute-api us-east-1 amazonaws com_Prod_ (1)](https://github.com/user-attachments/assets/a79f313e-2420-4adc-8bf1-e33c1c62cea8))

**[Check out the live project here!](https://lp0b66aa4h.execute-api.us-east-1.amazonaws.com/Prod/)**

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

The Bollywood Song Recommendation System is designed to recommend Bollywood songs to users based on their preferences. The system preprocesses the song data, trains a model, and provides a web interface for users to get song recommendations.

## Features

- **Data Preprocessing:** Clean and preprocess raw song data.
- **Model Training:** Train a recommendation model using machine learning techniques.
- **Web Interface:** A Flask-based web interface for users to input their preferences and get song recommendations.
- **Dockerized:** The project is containerized using Docker for easy deployment.
- **AWS Deployment:** Deployed on AWS Lambda and API Gateway for scalable and serverless architecture.

## Project Structure

```markdown
├── LICENSE
├── README.md              <- The top-level README for developers using this project.
├── data
│   ├── processed          <- The final, canonical data sets for modeling.
│   └── raw                <- The original, immutable data dump.
├── preprocessor           <- The preprocessor model.
├── models                 <- Trained and serialized models, model predictions, or model summaries.
├── notebooks              <- Jupyter notebooks.
├── requirements.txt       <- The requirements file for reproducing the analysis environment.
├── src                    <- Source code for use in this project.
│   ├── __init__.py        <- Makes src a Python module.
│   ├── base.py            <- Scripts that contain most utility functions.
│   ├── logger.py          <- Scripts to log the steps.
│   ├── data_preprocessing.py <- Scripts for data preprocessing.
│   └── model_training.py  <- Scripts to train models.
├── static
│   ├── css                <- The folder containing CSS files.
│   │   └── style.css      <- The file containing CSS classes.
│   ├── favicon.ico        <- Favicon for the web app.
│   └── images             <- The folder containing images required for the app.
├── templates
│   └── index.html         <- The file containing app HTML design.
├── .gitignore             <- Gitignore file.
├── .dvc                   <- DVC configuration file.
├── .dockerignore          <- Docker ignore file.
├── app.py                 <- Flask app.
├── dvc.lock               <- DVC lock file.
├── Dockerfile             <- Dockerfile for containerizing the app.
├── dvc.yaml               <- DVC pipeline configuration.
├── params.yaml            <- Parameters file.
├── README.Docker.md       <- README for Docker setup.
├── template.yaml          <- AWS Lambda and API Gateway template.yaml.
