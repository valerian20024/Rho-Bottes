FROM python:3

RUN useradd app
USER app

WORKDIR /home/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ data/
COPY src/ src/

CMD ["python3", "src/main.py"]