FROM public.ecr.aws/lambda/python:3.9

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/app.py ./
COPY data/raw/data.csv ./data/raw/
COPY models/similarity.pkl ./models/
COPY static/css/ ./static/css/
COPY static/images/ ./static/images/
COPY templates/ ./templates/

RUN chmod -R 755 ./static

CMD ["app.handler"]
