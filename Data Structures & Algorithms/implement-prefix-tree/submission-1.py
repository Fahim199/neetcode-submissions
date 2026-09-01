class PrefixTree:

    def __init__(self):
        self.letters = {}

    def insert(self, word: str) -> None:
        letters = self.letters
        for c in word:
            if c not in letters:
                letters[c]={}
            letters =letters[c]
        letters["end"] = None
                

    def search(self, word: str) -> bool:
        letters = self.letters
        for c in word:
            if c in letters:
                letters = letters[c]
                continue
            else:
                return False
        return "end" in letters
        

    def startsWith(self, prefix: str) -> bool:
        letters = self.letters
        for c in prefix:
            if c in letters:
                letters = letters[c]
                continue
            else:
                return False
        return True
        