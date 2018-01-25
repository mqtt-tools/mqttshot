########
mqttshot
########

mqttshot is a versatile little program for publishing and receiving images over MQTT.


********
Examples
********
::

    # Run example out of the box
    mqttshot --example

    # Send text and image from filesystem to specified topic and also raise the "alert" flag
    mqttshot --topic='testdrive/myhouse' --text='The house is on fire!' --image='/var/spool/house-on-fire.jpg' --alert

    # Send text and image from STDIN
    cat test.jpg | mqttshot --topic='testdrive/pipe' --text='An image from STDIN' --image=-

    # Send text and image from url
    mqttshot --topic='testdrive/pipe' --text='An image from the Internet' --image='https://images.unsplash.com/photo-1503022932596-500eb8cca2d8?w=100&q=10'

