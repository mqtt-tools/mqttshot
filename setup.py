import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'docopt',
    'requests',
    'paho-mqtt',
]

test_requires = [
]

setup(name='mqttshot',
  version='0.0.0',
  description='mqttshot is a versatile little program for publishing and receiving images over MQTT',
  long_description=README,
  license="AGPL 3",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Scientific/Engineering",
  ],
  author='Andreas Motl',
  author_email='andreas@getkotori.org',
  url='https://github.com/daq-tools/mqttshot',
  keywords='mqtt image transfer',
  packages=find_packages(),
  include_package_data=True,
  package_data={
  },
  zip_safe=False,
  test_suite='nose.collector',
  install_requires=requires,
  tests_require=test_requires,
  extras_require={
      'test': test_requires,
  },

  entry_points={
    'console_scripts': [
        'mqttshot      = mqttshot.command:run',
    ],
  },

)
