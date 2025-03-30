FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir streamlit pandas matplotlib xlsxwriter fpdf

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]