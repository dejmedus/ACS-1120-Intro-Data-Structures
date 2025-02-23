import random


class MarkovChain:
    def __init__(self, tokens):
        self.tokens = tokens
        self.chain = self.create_chain()

    def create_chain(self):
        chain = {}
        for i, token in enumerate(self.tokens):
            if i + 1 < len(self.tokens):
                next_word = self.tokens[i + 1]
                if token not in chain:
                    chain[token] = {}
                chain[token][next_word] = chain[token].get(next_word, 0) + 1
        return chain

    def random_walk(self, start_word, len=8):
        if start_word not in self.chain:
            raise Exception("No start word", start_word)

        path = [start_word]
        node = self.chain[start_word]
        for _ in range(len):
            # https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
            options = list(node.keys())
            next_token = random.choices(options, weights=node.values())[0]

            path.append(next_token)
            node = self.chain[next_token]

        return " ".join(path)
