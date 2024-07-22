# FROM public.ecr.aws/lambda/python:3.9

# WORKDIR ${LAMBDA_TASK_ROOT}

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY app.py ./
# COPY data/raw/data.csv ./data/raw/
# COPY models/similarity.pkl ./models/
# COPY static/css/ ./static/css/
# COPY static/images/ ./static/images/
# COPY templates/ ./templates/

# RUN chmod -R 755 ./static

# CMD ["app.handler"]






FROM public.ecr.aws/lambda/python:3.9

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure static files have the correct permissions
RUN chmod -R 755 static

CMD ["app.handler"]















# FROM python:3.9-slim
# WORKDIR /app
# COPY . /app
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8080
# ENV NAME World
# CMD ["python", "app.py"]
