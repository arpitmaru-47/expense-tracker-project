#STAGE 1: BUILDER
FROM python:3.12-slim AS builder 

WORKDIR /build 

COPY requirements.txt .

RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt 

#STAGE 2: RUNTIME
FROM python:3.12-slim AS runtime 

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/home/appuser 

WORKDIR /app

RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup \
    -m -d /home/appuser \
    -s /usr/sbin/nologin appuser && \
    mkdir -p /app/data && \
    chown -R 10001:10001 /app /home/appuser 

COPY --from=builder /opt/venv /opt/venv  

COPY --chown=10001:10001 app.py .
COPY --chown=10001:10001 templates/ templates/
COPY --chown=10001:10001 static/ static/                          

USER 10001:10001 

HEALTHCHECK --interval=30s \
  --timeout=5s \
  --start-period=10s \
  --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/', timeout=3)"

EXPOSE 5000


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info", "app:app"]
