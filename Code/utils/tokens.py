import re


def tokenize(content):
    parsed_content = re.sub('[^A-Za-z0-9]+', ' ', content)
    return parsed_content.split()
