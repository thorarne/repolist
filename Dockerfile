FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "repolist.py"]
