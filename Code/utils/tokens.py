import re


def tokenize(content):
    parsed_content = re.sub("[^<>'A-Za-z0-9,]+", " ", content)
    parsed_content = parsed_content.lower()

    return parsed_content.split()
