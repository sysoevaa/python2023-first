class Decrypter:
    def __init__(self, data: str):
        self.data = data
        for i in range(len(self.data)):
            if '0' <= data[i] <= '9':
                continue
            if 'a' <= data[i].lower() <= 'z':
                self.alphabet_size = 26
                self.first_letter = 'a'
                self.most_letter = 'e'
                break
            elif 'а' <= data[i].lower() <= 'я' or data[i].lower() == 'ё':
                self.alphabet_size = 33
                self.first_letter = 'а'
                self.most_letter = 'o'
            else:
                print("Unsupported alphabet. Please give data in russian or english")
                exit(1)

    def shift(self, delta: int, symbol: str) -> str:
        """Shifts symbol delta times in current alphabet. If alphabet ends,
         shift is beginning from start the alphabet"""

        pos = ord(symbol.lower()) - ord(self.first_letter) + delta
        pos %= self.alphabet_size
        return chr(ord(self.first_letter) + pos)

    def find_shift(self) -> int:
        for delta in range(self.alphabet_size):
            count = [[0, i] for i in range(self.alphabet_size)]
            letters = 0
            for i in range(len(self.data)):
                if self.data[i] in {'.', ',', ':', ';', '"', '!', '?', '(', ')', ' ', "'", '`', '’'}:
                    continue
                count[ord(self.shift(delta, self.data[i])) - ord(self.first_letter)][0] += 1
                letters += 1
            most_frequent = 0
            for i in range(len(count)):
                if count[i][0] > count[most_frequent][0]:
                    most_frequent = i
            if most_frequent == ord(self.most_letter) - ord(self.first_letter):
                return self.alphabet_size - delta
        return -1
