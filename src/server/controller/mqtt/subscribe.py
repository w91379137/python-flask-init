
from service import main
from flask import request
from ..tool import getValueInArgBody

def subscribe():
    topic = getValueInArgBody(request, 'topic')
    if topic is not None:
        main.mqtt.subscribe(topic)

    return topic
