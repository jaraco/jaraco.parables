from __future__ import annotations

import argparse
import itertools
import pathlib
import sys
from importlib.abc import Traversable
from typing import TYPE_CHECKING

from .config import config

if sys.version_info >= (3, 9):
    from importlib import resources

else:
    import importlib_resources as resources

if TYPE_CHECKING:
    from collections.abc import Iterable

    from _typeshed import StrOrBytesPath, StrPath
    from typing_extensions import SupportsIndex


def fixFormat(input_string: str) -> str:
    return input_string


def evaluatePhrase(inputString: str, config: config) -> str:
    if inputString.find('{') == -1:
        return inputString
    else:
        index1 = inputString.find('{')
        index2 = inputString.find('}')
        key = inputString[index1 + 1 : index2]

        # if the key is !, it's a subject
        if key == '!':
            phrase = config.get_subject()
        else:
            phrase = config.get_phrase(key)
        inputString = inputString[:index1] + phrase + inputString[index2 + 1 :]
        inputString = fixFormat(inputString)
        return evaluatePhrase(inputString, config)


def gen_phrase(config: config) -> str:
    output_string = config.get_phrase('starter')
    return evaluatePhrase(output_string, config)


def gen_phrases(
    filename: StrOrBytesPath | Iterable[StrOrBytesPath],
    number_of_outputs: SupportsIndex,
) -> None:
    loaded_config = config(filename)

    for i in range(0, number_of_outputs):
        loaded_config.create_subjects()
        print(gen_phrase(loaded_config))


def direct_or_package_file(spec: StrPath) -> Traversable:
    """
    Find a file either in this package or directly.

    >>> str(direct_or_package_file('self-reference'))
    '...self-reference.txt'
    """
    direct = pathlib.Path(spec)
    spec = str(spec)
    names = spec, spec + '.txt'
    package = (resources.files('jaraco.parables') / name for name in names)
    candidates = itertools.chain((direct,), package)
    try:
        return next(file for file in candidates if file.is_file())
    except StopIteration:
        raise ValueError(f"Couldn't find file {spec}")


def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=direct_or_package_file)
    parser.add_argument('-n', '--number_of_outputs', type=int, default=1)
    args = parser.parse_args()
    gen_phrases(**vars(args))
