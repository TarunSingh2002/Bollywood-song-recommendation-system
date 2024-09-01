# Bollywood Song Recommendation System

**[Check out the live project here!](https://lp0b66aa4h.execute-api.us-east-1.amazonaws.com/Prod/)**

Welcome to the Bollywood Song Recommendation System! This project uses machine learning to recommend Bollywood songs based on user-selected songs.

<table border="2" style="width:100%; border-collapse: collapse;">
  <tr>
    <td><img src="https://github.com/user-attachments/assets/6deccd80-3de7-470a-95ae-ba19b910dd95" alt="Project Image 1" style="width:100%;"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/74a78ed2-5c62-4e27-b5c3-91c7bde856a3" alt="Project Image 2" style="width:100%;"></td>
  </tr>
</table>

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Deployment](#deployment)
7. [License](#license)

## Project Overview

The Bollywood Song Recommendation System is designed to recommend Bollywood songs to users based on their selected songs. The system preprocesses the song data, trains a model, and provides a web interface for users to get song recommendations.

## Features

- **Data Preprocessing:** Clean and preprocess raw song data.
- **Model Training:** Train a recommendation model using machine learning techniques.
- **Web Interface:** A Flask-based web interface for users to select a song and get recommendations for 10 similar songs.
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
```
## Installation

To get a copy of the project up and running on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/bollywood-song-recommendation-system.git
    cd bollywood-song-recommendation-system
    ```

2. **Set up a virtual environment:**
    ```bash
    conda create --name song-recommendation-system python=3.9
    conda activate song-recommendation-system
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Build and run the Docker container:**
    ```bash
    docker build -t song-recommendation-system .
    docker run -p 5000:5000 song-recommendation-system
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your browser and go to:**
    ```
    http://localhost:5000
    ```

3. **Select a song from the dropdown and get recommendations for similar songs.**

## Deployment

### Deploying to AWS Lambda and API Gateway

1. **Ensure you have AWS CLI installed and configured:**
    ```bash
    aws configure
    ```

2. **Build and push the Docker image to Amazon ECR:**
    ```bash
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-east-1.amazonaws.com
    docker tag song-recommendation-system:latest <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/song-recommendation-system:latest
    docker push <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/song-recommendation-system:latest
    ```

3. **Deploy the application using AWS SAM:**
    ```bash
    sam build --template-file template.yaml
    sam deploy --guided
    ```

4. **Follow the prompts to complete the deployment.**

## License

```markdown
MIT License

Copyright (c) 2024 Tarun Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
