FROM python:3.11-slim AS runtime
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "src.api.fantasyRestAPI:app"]