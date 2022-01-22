import string


def code(text: str, shift: int):
    word_code = ''

    for i in text:
        if i.isalpha():
            letter = ord(i)
            letter += shift

            if i.isupper():
                if letter > 90:
                    letter -= 26
                elif letter < 65:
                    letter += 26

            else:
                if letter > 122:
                    letter -= 26
                elif letter < 97:
                    letter += 26

            word_code += chr(letter)

        else:
            word_code += i

    return word_code


print(code('abcdefz', 3))

print('-' * 30)

# NEW CODE ! UPDATE!


def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


code_text = 'Hello World! My name is Peter!'
print(caesar(code_text, 10, [string.ascii_lowercase,
      string.ascii_uppercase, string.punctuation]))
