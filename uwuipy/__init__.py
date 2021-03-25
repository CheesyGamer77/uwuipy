import validators
import random
from typing import Optional, Sequence


class Uwuifier:
    def __init__(
        self,
        faces: Optional[Sequence[str]] = None,
        exclamations: Optional[Sequence[str]] = None,
        actions: Optional[Sequence[str]] = None
    ):
        self._spaceModifier = {
            "faces": 0.05,
            "actions": 0.075,
            "stutters": 0.1
        }
        self._wordModifier = 1
        self._exclamationModifier = 1

        self.faces = faces if faces is not None else [
            '(・`ω´・)',
            ';;w;;',
            'OwO',
            'UwU',
            '>w<',
            '^w^',
            'ÚwÚ',
            '^-^',
            ':3',
            'x3'
        ]

        self.exclamations = exclamations if exclamations is not None else [
            '!?', '?!!', '?!?1', '!!11', '?!?!'
        ]

        self.actions = actions if actions is not None else [
            '*blushes*',
            '*whispers to self*',
            '*cries*',
            '*screams*',
            '*sweats*',
            '*twerks*',
            '*runs away*',
            '*screeches*',
            '*walks away*',
            '*sees bulge*',
            '*looks at you*',
            '*notices buldge*',
            '*starts twerking*',
            '*huggles tightly*',
            '*boops your nose*'
        ]

    def _word_mapper(self, word: str) -> str:
        if validators.url(word):
            return word

        if random.random() <= self._wordModifier:
            word = word.replace("r", "w").replace("R", "W").replace("ove", "uv")
        
        return word

    def uwuify_words(self, text: str) -> str:
        return " ".join(list(map(self._word_mapper, text.split(" "))))
    
    def uwuify_spaces(self, text: str) -> str:
        words = text.split(" ")

        out_words = []

        for word in words:
            val = random.random()
            if val <= self._spaceModifier["faces"]:
                word += " " + random.choice(self.faces)
            elif val <= self._spaceModifier["actions"]:
                word += " " + random.choice(self.actions)
            elif val <= self._spaceModifier["stutters"]:
                word = " " + word[0] + "-" + word[0].lower() + word[1:]
            
            out_words.append(word)
        
        return " ".join(out_words)
    
    def uwu(self, text: str) -> str:
        out = self.uwuify_words(text)
        out = self.uwuify_spaces(out)
        return out    


if __name__ == "__main__":
    uwuifier = Uwuifier()

    text = "This library is not on pip as of right now."

    print(f"Original Text: \"{text}\"\nUwUified Text: \"{uwuifier.uwu(text)}\"")
        