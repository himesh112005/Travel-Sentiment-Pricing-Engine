# Base Image
FROM python:3.12-slim

# Set Working Directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install streamlit plotly pandas nltk

# Copy the rest of the application code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]