import re


def get_source_text(filename):
    with open(filename, "r") as file:
        content = file.read().lower()
        return re.sub('[^A-Za-z0-9]+', ' ', content)


def histogram(source_text):
    word_count = {}
    for word in source_text.split():
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram.get(word, 0)


def sample(histogram):
    sorted_list = sorted(histogram.items(), key=lambda x: x[1])
    return sorted_list[-1][0]


if __name__ == "__main__":
    source_text = get_source_text('./Code/data/sample.txt')
    hist = histogram(source_text)

    # print(hist)
    # print(unique_words(hist))
    # print(frequency("red", hist))
    # print(sort_histogram(hist))
    print(sample(hist))
