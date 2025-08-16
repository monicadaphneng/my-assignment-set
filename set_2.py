'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift a single letter by a given number of steps.

    Wraps around the alphabet if necessary. Spaces remain unchanged.

    Parameters
    letter: str
        a single uppercase letter or a space.
    shift: int
        the number of positions to move the letter forward.

    Returns
    str
        the resulting letter or a space if input was a space.
    '''
    if letter == " ":
        return " "
    else:
        x = (ord(letter) - ord("A") + shift) % 26
        return chr(ord("A") + x)


def caesar_cipher(message, shift):
    '''Shift every letter in a message by a fixed number of steps.

    Spaces are left untouched. Implements the classic Caesar cipher.

    Parameters
    message: str
        uppercase letters and spaces.
    shift: int
        number of positions each letter is moved forward.

    Returns
    str
        encoded message.
    '''
    encoded = ""
    for letter in message:
        encoded += shift_letter(letter, shift)
    return encoded


def shift_by_letter(letter, letter_shift):
    '''Shift a letter using another letter as the shift value.

    'A' represents 0, 'B' is 1, ..., 'Z' is 25.
    Spaces remain unchanged.

    Parameters
    letter: str
        a single uppercase letter or space.
    letter_shift: str
        uppercase letter defining the shift.

    Returns
    str
        shifted letter or space.
    '''
    if letter == " ":
        return " "
    shift = ord(letter_shift) - ord("A")
    return shift_letter(letter, shift)


def vigenere_cipher(message, key):
    '''Encrypt a message using a keyphrase for variable shifts.

    Each letter is shifted by the corresponding key letter's value.
    Spaces in the message are ignored but preserved.

    Parameters
    message: str
        uppercase letters and spaces.
    key: str
        uppercase letters, repeated as needed to match message length.

    Returns
    str
        encrypted message.
    '''
    result = []
    key_index = 0
    for char in message:
        if char == ' ':
            result.append(' ')
        else:
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(shift_letter(char, shift))
            key_index += 1
    return ''.join(result)


def scytale_cipher(message, shift):
    '''Simulate a scytale cipher on a message.

    Pads message with underscores if needed, then rearranges characters
    according to a columnar wrapping scheme.

    Parameters
    message: str
        uppercase letters and underscores (underscore = space).
    shift: int
        number of rows (or the cylinder's circumference).

    Returns
    str
        rearranged (encrypted) message.
    '''
    if len(message) % shift != 0:
        padding = shift - (len(message) % shift)
        message += "_" * padding
    
    encoded = ""
    columns = len(message) // shift
    for i in range(len(message)):
        index = (i // shift) + columns * (i % shift)
        encoded += message[index]
    return encoded


def scytale_decipher(message, shift):
    '''Decrypt a message encoded with scytale_cipher.

    Reverses the columnar rearrangement to recover original text.

    Parameters
    message: str
        uppercase letters and underscores (underscore = space).
    shift: int
        number of rows used in the cipher.

    Returns
    str
        decrypted message.
    '''
    columns = len(message) // shift
    decoded = [""] * len(message)
    for i in range(len(message)):
        index = (i // columns) + shift * (i % columns)
        decoded[i] = message[index]
    return "".join(decoded)