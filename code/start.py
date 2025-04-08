import sys
import ciphers
import files
import decoder

def caesar() -> int:
    """Function realise communication with user in case caesar encryption.
    Returns one number -- size of shift for caesar encryption """

    print("Please, enter size of shift. It should be >0 if it will be right shift. Otherwise it will be left shift.")
    shift = input()
    for i in range(len(shift)):
        if shift[i] == '-':
            if i != 0:
                print("Please enter the correct shift")
                exit(1)

        if (ord(shift[i]) < ord('0') or ord(shift[i]) > ord('9')) and shift[i] != '-':
            print("Please enter the correct shift")
            exit(1)
    return int(shift)


def main() -> None:
    """Main function for the beginning and entering the parameters for encryption"""

    argv = sys.argv
    if len(argv) < 2:
        print("Not enough arguments to start\n")
        print("Please run in this order: python3 main.py <input file name.extension> "
              "<output file name.extension>(optional)\n")
        print("You also can write no output file and the result will be written in file "
              "<input file name>_encrypted.txt in the same folder")
        exit(1)
    input_file = files.Files(argv[1])
    input_data = input_file.read()
    if len(argv) == 2:
        output_file = (input_file.get_path() + '/' + input_file.get_name_without_extension() +
                       '_encrypted.' + input_file.get_extension())
    else:
        output_file = argv[2]

    if len(argv) == 2:
        output_file = files.Files(output_file, False)
    else:
        output_file = files.Files(output_file)

    print("Please, enter type of encryption. Supporting variants: caesar (1), vernam (2), vigenere (3), frequency(4)")
    encryption_type = input()
    cipher = ciphers.Ciphers(input_data)
    if encryption_type == '1' or encryption_type == 'caesar':
        shift = caesar()
        cipher.caesar(shift)
    elif encryption_type == '2' or encryption_type == 'vernam':
        cipher.vernam()
    elif encryption_type == '3' or encryption_type == 'vigenere':
        print("Please, enter the code word for encryption or write 0 for random word")
        code_word = input()
        cipher.vigenere(code_word)
    elif encryption_type == '4' or encryption_type == 'frequency':
        decode = decoder.Decrypter(input_data)
        output_file.write(str(decode.find_shift()))
        exit(0)
    else:
        print("Unsupported type of encryption")
        exit(1)
    output_file.write(cipher.answer)

