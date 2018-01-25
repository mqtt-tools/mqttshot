# -*- coding: utf-8 -*-
# (c) 2018 Andreas Motl <andreas@getkotori.org>
import os
import sys
import json
import base64
import requests
import paho.mqtt.client as mqtt
from collections import OrderedDict


def client_factory(broker):
    client = mqtt.Client()
    client.connect(broker, 1883, 60)
    client.on_publish = on_publish
    return client


def on_publish(srv, userdata, mid):
    srv.disconnect()


def publish_rich_media(broker='localhost', topic='testdrive', **kwargs):

    client = client_factory(broker)

    # The MQTT message
    message = OrderedDict()

    # Add multiple fields to message with appropriate encoding

    # The "text" field
    if 'text' in kwargs:
        message['text'] = kwargs['text']

    # The "image" field
    if 'image' in kwargs and kwargs['image']:

        # Acquire image payload from various sources
        image = kwargs['image']

        # Let's read it from STDIN
        if image == '-':
            image_payload = sys.stdin.read()

        # If it exists on the file system, read it from there
        elif os.path.exists(image):
            f = open(image, "rb")
            image_payload = f.read()
            f.close()

        # If it looks like an url, get it from the Internet
        elif image.startswith('http'):
            image_payload = requests.get(image).content

        else:
            raise ValueError('Image {} could not be acquired'.format(image))

        # Encode image to Base64
        message['image'] = base64.b64encode(image_payload)

    client.publish(topic, json.dumps(message), 0)
    client.loop_forever()
