FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY app.py app.py
RUN mkdir -p /app/static
RUN mkdir -p /app/templates
COPY templates/* templates/.
COPY static/* static/.


CMD ["flask", "run", "--host", "0.0.0.0"]
