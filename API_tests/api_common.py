
import requests as r
import json
import setup
import logging
logger = logging.getLogger(__name__)


def get_request(url, headers=None, auth=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return r.get(url, headers=temphead, auth=auth)


def post_request(url, headers=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return r.post(url, headers=temphead)

def put_request(url, headers=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return r.put(url, headers=temphead)
