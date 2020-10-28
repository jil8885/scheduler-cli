from os.path import abspath, dirname, join

from setuptools import find_packages, setup

from scheduler import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst')) as file:
    long_description = file.read()




setup(
    name = 'scheduler_todo',
    version = __version__,
    description = 'A scheduler command line program in Python.',
    long_description = long_description,
    url = 'https://github.com/jil8885/scheduler-cli',
    author = 'Jeongin Lee',
    author_email = 'jil8885@hanynag.ac.kr',
    license = 'MIT LICENSE',
    classifiers = [
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords = ['cli','scheduler-cli'],
    packages = find_packages(),
    install_requires = ['termcolor', 'colorama', 'flask', 'requests','websocket-client','slacker'],
    entry_points = {
        'console_scripts': [
            'scheduler-cli=scheduler.main:main_scheduler',
            'scheduler-server=server.main:scheduler_server',
            'scheduler-slack=slackbot.main:slack_server',
        ],
    },
)
