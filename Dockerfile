FROM python:3.9-slim-buster
EXPOSE 8501
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install streamlit

COPY . .

ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]


