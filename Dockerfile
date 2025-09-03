# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better build caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download NLTK vader_lexicon so it’s ready at runtime
RUN python -m nltk.downloader vader_lexicon

# Copy the rest of the app
COPY . .

# Expose Flask port
EXPOSE 5002

# Run the app
CMD ["python", "app.py"]
