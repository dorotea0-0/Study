class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        if not self.word:
            return ""
        return self.word[0].upper() + self.word[1:].lower()

    def __repr__(self):
        return f"Word('{self.word}')"

    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) == len(other.word)

    def __ne__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) != len(other.word)

    def __gt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) > len(other.word)

    def __lt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) < len(other.word)

    def __ge__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) >= len(other.word)

    def __le__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) <= len(other.word)


# Пример использования
word1 = Word('Hellow')
word2 = Word('world!')

print(word1 > word2)
print(word1 < word2)
print(word1 == word2)