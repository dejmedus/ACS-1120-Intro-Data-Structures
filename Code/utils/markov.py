import random


class MarkovChain(dict):
    def __init__(self, tokens):
        super().__init__()

        self.tokens = tokens
        self.chain_tokens()

    def chain_tokens(self):
        for i, token in enumerate(self.tokens):
            if i + 1 < len(self.tokens):
                next_word = self.tokens[i + 1]
                if token not in self:
                    self[token] = {}
                self[token][next_word] = self[token].get(next_word, 0) + 1

    def random_walk(self, start_word, len=20):
        if start_word not in self:
            raise Exception("No start word", start_word)

        path = [start_word]
        node = self[start_word]
        for _ in range(len):
            # https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
            options = list(node.keys())
            next_token = random.choices(options, weights=node.values())[0]

            path.append(next_token)
            node = self[next_token]

        return " ".join(path)
