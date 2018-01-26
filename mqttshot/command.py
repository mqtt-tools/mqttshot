# -*- coding: utf-8 -*-
# (c) 2018 Andreas Motl <andreas@getkotori.org>
from docopt import docopt
from mqttshot.core import publish_rich_media


def run():
    """
    Usage:
      mqttshot [--broker=] --topic= --text= --image= [--alert]
      mqttshot [--broker= --topic= --text= --image= --alert] --example
      mqttshot --version
      mqttshot (-h | --help)

    Examples:

      # Run example out of the box
      mqttshot --example

      # Send text and image from filesystem to specified topic and also raise the "alert" flag
      mqttshot --topic='testdrive/myhouse' --text='The house is on fire!' --image='/var/spool/house-on-fire.jpg' --alert

      # Send text and image from STDIN
      cat test.jpg | mqttshot --topic='testdrive/pipe' --text='An image from STDIN' --image=-

      # Send text and image from url
      mqttshot --topic='testdrive/pipe' --text='An image from the Internet' --image='https://images.unsplash.com/photo-1503022932596-500eb8cca2d8?w=100&q=10'

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

    # Use reasonable defaults
    # FIXME: Do this using docopt
    if 'broker' not in options:
        options['broker'] = 'localhost'
    if 'topic' not in options:
        options['topic'] = 'testdrive'

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
