FROM python:3.11-slim
WORKDIR /app
COPY app/main.py ./main.py
RUN python -m py_compile main.py
EXPOSE 8000
CMD ["python", "main.py"]
