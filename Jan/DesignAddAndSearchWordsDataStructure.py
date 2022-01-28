class WordDictionary:
    word_list = []

    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        self.word_list.append(word)

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.word_list
        else:
            p = re.compile(word)
            for in_word in self.word_list:
                if p.match(in_word):
                    return True
            return False