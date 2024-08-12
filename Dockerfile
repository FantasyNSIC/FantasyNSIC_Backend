FROM python AS runtime
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "src.api.fantasyRestAPI"]