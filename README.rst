.. image:: https://img.shields.io/pypi/v/jaraco.parables.svg
   :target: https://pypi.org/project/jaraco.parables

.. image:: https://img.shields.io/pypi/pyversions/jaraco.parables.svg

.. image:: https://github.com/jaraco/jaraco.parables/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.parables/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2024-informational
   :target: https://blog.jaraco.com/skeleton

Python library based on `XKCD 1263: Reassuring <https://xkcd.com/1263/>`_.

Based on `Reassuring-Parable-Generator
<https://github.com/JackToaster/Reassuring-Parable-Generator>`_,
it generates thousands of reassuring parables about things humans
are better than computers at every second.

Usage
=====

To use the program, pass the filename of the .cfg you would like to use.

Several files are included:

1. reassuring - The standard reassuring parable generator.
2. self-reference - A test file that generates statements about the text generator program.
3. trump - A popular US President.

Example
-------

    $ python -m jaraco.parables reassuring -n 20
    Computers won't be able to understand a piece of music.
    A computer never will be able to experience eating a cookie.
    A computer won't experience eating a salad.
    A computer will never enjoy a poem.
    A computer won't ever be able to understand a poem.
    Computers will never experience a wonderful piece of music.
    A computer can't understand a song.
    Computers won't be able to experience eating a cake.
    A computer will never have the ability to enjoy a song.
    Computers will never be able to understand a sonnet.
    A computer isn't capable of enjoy a song.
    A computer will never be able to experience eating a chicken dinner.
    Computers won't ever be able to experience a superb sonnet.
    No computer is capable of taste a piece of pie.
    Computers never will be able to enjoy a amazing sonnet.
    Computers will never be able to experience eating a cake.
    A computer isn't capable of experience a beautiful poem.
    Computers will never have the ability to enjoy a superb sonnet.
    Computers won't ever be able to experience a story.
    Computers will never have the ability to experience a play.
