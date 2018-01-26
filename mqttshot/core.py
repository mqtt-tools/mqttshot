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
    """
    Connect to MQTT broker
    TODO: Obtain port and timeout from function arguments.
    """
    client = mqtt.Client()
    client.connect(broker, 1883, 60)
    client.on_publish = on_publish
    return client


def on_publish(srv, userdata, mid):
    srv.disconnect()


def publish_rich_media(broker='localhost', topic='testdrive', **kwargs):

    # The MQTT client handle
    client = client_factory(broker)

    # The MQTT message
    message = OrderedDict()

    # Add multiple fields to message with appropriate encoding

    # Special handling for the "image" field:
    # Acquire image from source and encode with base64
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

        # Encode image to base64
        message['image'] = base64.b64encode(image_payload)

        del kwargs['image']

    # Propagate all other fields from kwargs verbatim
    for key, value in kwargs.items():
        if value is not None:
            message[key] = value

    # Serialize message to JSON
    payload = json.dumps(message)

    # Publish to MQTT bus
    client.publish(topic, payload, 0)

    # Process
    client.loop_forever()

