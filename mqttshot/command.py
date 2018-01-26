# -*- coding: utf-8 -*-
# (c) 2018 Andreas Motl <andreas@getkotori.org>
from docopt import docopt
from mqttshot.core import publish_rich_media


def run():
    """
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

    Miscellaneous options:

      --version                 Show version information
      -h --help                 Show this screen
    """

    # Read commandline options
    options = normalize_docopt_options(docopt(run.__doc__, version='mqttshot 0.0.0'))

    # Either run the example out of the box
    if options['example']:

        # Filter None values
        clean_options = {key: value for key, value in options.items() if value is not None}

        # Get example message
        options = example()

        # Let fields be overridable from command line arguments
        options.update(clean_options)

    else:
        # Filter None values
        options = {key: value for key, value in options.items() if value is not None}

    # Apply reasonable defaults
    options.setdefault('broker', 'localhost')
    options.setdefault('topic', 'testdrive')
    options.setdefault('text', None)
    options.setdefault('alert', False)

    # Publish message to MQTT
    publish_rich_media(
        broker=options['broker'],
        topic=options['topic'],
        text=options['text'],
        image=options['image'],
        alert=options['alert'],
    )


def example():
    return dict(
        topic='testdrive/australia',
        text='Surfing!',
        image='https://images.unsplash.com/photo-1503022932596-500eb8cca2d8?w=100&q=10',
        alert=False,
    )


def normalize_docopt_options(options):
    normalized = {}
    for key, value in options.items():
        key = key.strip('--<>')
        normalized[key] = value
    return normalized


if __name__ == '__main__':
    run()
