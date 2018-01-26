########
mqttshot
########


About
=====
mqttshot is a versatile little program for publishing and receiving images over MQTT.


Features
========
- Offer flexible image acquisition from different sources.
  You can currently choose from File, URL and STDIN.
- Use base64 for encoding the image, it feels safer than "just binary"
  and can be used to encapsulate the image into a message container.
- Use JSON as message container format, as you usually want to send more data along.
  In the current implementation, the message structure is very simple
  and not restricted by any schema::

    {
        "text": "The car is on fire!",
        "image": "/9j/4AAQSkZJRgAB ... JooA/9k=",
        "alert": true
    }


Background
==========
Please consider this as a proposal about a simple convention of how to
send basic messages containing images over MQTT. We will be happy if
this of any interest for you and love to hear back from you.

This was built to support the creation of a new feature for mqttwarn_,
namely `Add support for Pushover image attachments`_.

.. _mqttwarn: https://github.com/jpmens/mqttwarn
.. _Add support for Pushover image attachments: https://github.com/jpmens/mqttwarn/issues/284


Synopsis
========
::

    $ mqttshot --help

    Usage:
        mqttshot --topic= --image= [--broker=] [--text=] [--alert]
        mqttshot --example [--broker= --topic= --text= --image= --alert]
        mqttshot --version
        mqttshot (-h | --help)

    Examples:

      # Run example out of the box: Publish a message with an image
      # to a MQTT broker running on "localhost" to the topic "testdrive"
      mqttshot --example

      # Publish image acquired from filesystem with text from command line argument
      # to specified topic and also raise the "alert" flag
      mqttshot --topic='testdrive/home' --text='The house is on fire!' --image='/var/spool/house-on-fire.jpg' --alert

      # Publish image acquired from STDIN
      cat test.jpg | mqttshot --topic='testdrive/pipe' --image=-

      # Publish image acquired from HTTP URL
      mqttshot --topic='testdrive/url' --image='https://images.unsplash.com/photo-1503022932596-500eb8cca2d8?w=100&q=10'


References
==========
There are other discussions and projects about sending and receiving images over MQTT.

Projects
--------
- https://github.com/suknuk/MQTT-Images
- https://play.google.com/store/apps/details?id=it.barbaro.zanzito

Tutorials
---------
- How to Send a File Using MQTT Using a Python Script
  http://www.steves-internet-guide.com/send-file-mqtt/

- Node-RED

    - https://dennisschultz.wordpress.com/2015/06/29/my-internet-of-things-and-mobilefirst-adventure-part-5-adding-in-the-camera/
    - https://dennisschultz.wordpress.com/2016/02/05/part-7-requesting-and-receiving-a-picture/

- Home Assistant

    - https://home-assistant.io/components/camera.mqtt/
    - https://github.com/home-assistant/home-assistant/blob/master/homeassistant/components/camera/mqtt.py
    - https://github.com/home-assistant/home-assistant/blob/master/tests/components/camera/test_mqtt.py

- https://community.hortonworks.com/articles/77988/ingest-remote-camera-images-from-raspberry-pi-via.html

Discussions
-----------
- https://stackoverflow.com/questions/37499739/how-can-i-send-a-image-by-using-mosquitto
- https://forum.pycom.io/topic/1133/camera-image-over-mqtt
