FROM python:3.12

WORKDIR /app

RUN apt-get update && \
    apt-get install -y vim nano

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "index.py", "--server.port", "8501", "--browser.serverAddress", "0.0.0.0", "--client.toolbarMode", "viewer", "--theme.base", "dark", "--theme.primaryColor", "#076deb"]