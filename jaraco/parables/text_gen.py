import argparse
from .config import config


def fixFormat(input_string):
    return input_string


def evaluatePhrase(inputString, config):
    if inputString.find('{') == -1:
        return inputString
    else:
        index1 = inputString.find('{')
        index2 = inputString.find('}')
        key = inputString[index1 + 1:index2]

        # if the key is !, it's a subject
        if key == '!':
            phrase = config.get_subject()
        else:
            phrase = config.get_phrase(key)
        inputString = inputString[:index1] + phrase + inputString[index2 + 1:]
        inputString = fixFormat(inputString)
        return evaluatePhrase(inputString, config)


def gen_phrase(config):
    output_string = config.get_phrase('starter')
    return evaluatePhrase(output_string, config)


def gen_phrases(filename, number_of_outputs):
    loaded_config = config(filename)

    for i in range(0, number_of_outputs):
        loaded_config.create_subjects()
        print(gen_phrase(loaded_config))


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-n', '--number_of_outputs', type=int)
    return parser.parse_args()
