# Multi-stage build for Python application
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt* ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || echo "No requirements.txt"

# Copy application code
COPY . .

# Production stage
FROM python:3.11-slim

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copy from builder
COPY --from=builder /app /app

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-u", "main.py"]