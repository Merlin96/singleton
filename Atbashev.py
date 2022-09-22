lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}


def atbash(message):
    cipher = ''
    for i in message:
        if (i != ' '):
            # adds the corresponding letter from the lookup_table
            cipher += lookup_table[i]
        else:
            # adds space
            cipher += ' '

    return cipher
# Driver function to run the program
# encrypt the given message
kek = input()

print(atbash(kek.upper()))
#decipher
ciphered = atbash(kek.upper())
print(atbash(ciphered.upper()))
