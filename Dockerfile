FROM nikolaik/python-nodejs:latest

COPY . .

WORKDIR /backend

RUN pip install -r requirements.txt

WORKDIR ..

EXPOSE 3000

CMD ["npm", "start"]