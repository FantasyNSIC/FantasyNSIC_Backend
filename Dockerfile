FROM python AS runtime
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "src.api.fantasyRestAPI:app"]