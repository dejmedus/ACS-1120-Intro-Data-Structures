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

        return self.spell(path)

    def spell(self, path):
        spell = " ".join(path)
        def low_num(): return str(random.randint(1, 9))
        def high_num(): return str(random.randint(10, 120))
        def dice_roll(): return f"{low_num()}+{low_num()}d"
        def ordinal(): return f"{random.randint(4, 12)}th"

        while "<negnum>" in spell:
            spell = spell.replace("<negnum>", f"-{low_num()}", 1)
        while "<roll>" in spell:
            spell = spell.replace("<roll>", dice_roll(), 1)
        while "<lownum>" in spell:
            spell = spell.replace("<lownum>", low_num(), 1)
        while "<highnum>" in spell:
            spell = spell.replace("<highnum>", high_num(), 1)
        while "<ordinal>" in spell:
            spell = spell.replace("<ordinal>", ordinal(), 1)

        spell = spell.replace(" <end>", ". ")
        spell = spell.strip()

        sentences = spell.split(".")
        if len(sentences) > 1:
            spell = sentences[0]

        spell = spell.capitalize()

        return spell
