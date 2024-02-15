import time

from celery import Celery

from backend.core import create_app
from backend.core.config import settings

app = create_app()

celery = Celery(
    __name__,
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@celery.task
def div(x, y):
    time.sleep(5)
    return x / y


@celery.task
def mod(x, y):
    time.sleep(5)
    return x % y


@celery.task
def mult(x, y):
    time.sleep(5)
    return x * y


@celery.task
def sum(x, y):
    time.sleep(5)
    return x + y


@celery.task
def diff(x, y):
    time.sleep(5)
    return x - y
