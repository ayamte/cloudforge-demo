FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt
RUN python -m pip uninstall -y pip
COPY app.py /app/
CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]