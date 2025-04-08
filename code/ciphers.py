import random

class Ciphers:
    """Class for caesar, vigenere and vernam encryption.
    Takes the source text and moves it via one of supporting encryption"""

    def __init__(self, start):
        self.non_encrypted = start
        self.ru_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        self.en_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z']
        self.answer = ""
        self.code_ru = ""
        self.no_spaces = ''.join(self.non_encrypted.split(sep=' '))

    def caesar(self, delta):
        """Realise Caesar encryption with current shift"""

        for c in self.non_encrypted:
            if not c.isalpha():
                self.answer += c
                continue
            self.answer += self.shift(delta, c)

    def vigenere(self, code_word):
        """Realise Vigenere encryption with given code word or
        takes the random code word and write it in console"""

        if code_word == '0':
            code_word = ''
            for i in range(max(len(self.non_encrypted) // 200, 10)):
                code_word += chr(random.randint(0, 25) + ord('a'))
            print(code_word)
        for i in range(len(self.non_encrypted)):
            if not self.non_encrypted[i].isalpha():
                self.answer += self.non_encrypted[i]
            else:
                self.answer += self.shift(ord(code_word[i % len(code_word)]) - ord('a'), self.non_encrypted[i], i)

    def vernam(self):
        """Realise Vernam with random source string"""
        rand_word = ''
        for i in range(max(len(self.non_encrypted) // 300, 3)):
            rand_word += chr(random.randint(0, 25) + ord('a'))
        for i in range(len(self.non_encrypted)):
            if not self.non_encrypted[i].isalpha():
                self.answer += self.non_encrypted[i]
            else:
                self.answer += str(ord(self.non_encrypted[i]) ^ ord(rand_word[i % len(rand_word)]))
            self.answer += ' '

    def shift(self, delta: int, symbol: str, index: int = 1) -> str:
        """Shifts symbol delta times in current alphabet. If alphabet ends,
         shift is beginning from start the alphabet"""

        is_low = True
        if symbol.lower() != symbol:
            is_low = False

        if ord('a') <= ord(symbol.lower()) <= ord('z'):
            pos = ord(symbol.lower()) - ord('a') + delta
            pos %= len(self.en_alphabet)
            if is_low:
                return self.en_alphabet[pos]
            return self.en_alphabet[pos].upper()

        if ord('а') <= ord(symbol.lower()) <= ord('я') or symbol.lower() == 'ё':
            pos = ord(symbol.lower()) - ord('а') + delta
            pos %= len(self.ru_alphabet)
            if is_low:
                return self.ru_alphabet[pos]
            return self.ru_alphabet[pos].upper()
        print("Unsupported language, please give text in english or russian")
        print(symbol)
        print(index)
        exit(1)
