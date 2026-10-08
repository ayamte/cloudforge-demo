FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip uninstall -y pip
COPY app.py /app/
RUN useradd --uid 10001 --create-home appuser
USER appuser
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]