
from asabulu.service import main
from flask import request
from ..tool import getValueInArgBody

def publish():
    topic = getValueInArgBody(request, 'topic')
    msg = getValueInArgBody(request, 'msg')
    if topic is not None:
        main.mqtt.publish(topic, msg)

    return f'{topic}: {msg}'