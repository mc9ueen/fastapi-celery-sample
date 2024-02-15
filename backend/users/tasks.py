import time

from celery import shared_task


@shared_task
def div(x, y):
    time.sleep(5)
    return x / y


@shared_task
def mod(x, y):
    time.sleep(5)
    return x % y


@shared_task
def mult(x, y):
    time.sleep(5)
    return x * y


@shared_task
def sum(x, y):
    time.sleep(5)
    return x + y


@shared_task
def diff(x, y):
    time.sleep(5)
    return x - y
