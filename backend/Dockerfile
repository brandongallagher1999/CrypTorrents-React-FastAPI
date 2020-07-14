FROM python:latest

COPY . .

RUN pip install -r requirements.txt

#EXPOSE port 5000 for Uvicorn server
EXPOSE 5000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]