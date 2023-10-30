def remove_duplicates(text):
    return ''.join(sorted(set(text), key=text.index))

def generate_alphabet(key, alphabet):
    key = remove_duplicates(key)
    key += alphabet
    key = remove_duplicates(key)
    return key

def polyalphabetic_cipher(plaintext, keys, alphabet):
    ciphertext = ''
    for key in keys:
        key = generate_alphabet(key, alphabet)
        for char in plaintext:
            if char in alphabet:
                index = alphabet.index(char)
                ciphertext += key[index]
            else:
                ciphertext += char
        plaintext = ciphertext
        ciphertext = ''
    return ' '.join(plaintext.upper())  # Menambahkan spasi pada hasil ciphertext

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keys = ['merdeka', 'indonesia', 'putihmerah']  # Tiga kunci
    plaintext = input("Masukkan plaintext: ")

    plaintext = plaintext.lower()
    ciphertext = polyalphabetic_cipher(plaintext, keys, alphabet)

    print("Ciphertext:", ciphertext)  # Mencetak hasil ciphertext dengan spasi

if __name__ == '__main__':
    main()
