FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["Streamlit", "run", "app.py", "--server.port=7860", "server.address=0.0.0.0"]
