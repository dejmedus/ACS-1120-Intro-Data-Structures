import random

from data.in_words import IN_WORDS


class MarkovChain(dict):
    def __init__(self, tokens, n=2):
        super().__init__()
        self.tokens = tokens
        self.n = n
        self.chain_tokens()

    def chain_tokens(self):
        for i in range(len(self.tokens) - self.n):
            token = tuple(self.tokens[i:i + self.n])
            next_token = self.tokens[i + self.n]

            if token not in self:
                self[token] = {}

            self[token][next_token] = self[token].get(next_token, 0) + 1

    def random_walk(self, len=20):
        start_words = random.choice(IN_WORDS[self.n])
        start_words = tuple(start_words.lower().split())

        if start_words not in self:
            raise Exception("No start words", start_words)

        path = list(start_words)
        curr_tup = start_words

        for _ in range(len):
            if curr_tup not in self:
                break
            # https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
            next_token = random.choices(
                list(self[curr_tup].keys()), weights=self[curr_tup].values())[0]

            path.append(next_token)
            curr_tup = tuple(path[-self.n:])

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

        spell = spell.replace(" <end>", " ")
        spell = spell.strip()
        return spell.capitalize()
