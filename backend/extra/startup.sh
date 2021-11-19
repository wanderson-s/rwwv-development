#docker build -t api_budget:v1 --platform linux/amd64 .

gunicorn \
    --bind 0.0.0.0:8000 \
    -w 1 \
    -k "uvicorn.workers.UvicornWorker" \
    "main:create_app()"