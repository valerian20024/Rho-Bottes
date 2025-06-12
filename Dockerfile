FROM python:3.13-slim-bookworm

WORKDIR /home/app

# todo: use a virtual environment instead

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY data/ data/
COPY src/ src/

RUN useradd app
USER app

CMD ["python3", "src/main.py"]