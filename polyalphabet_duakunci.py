def remove_duplicates(text):
    return ''.join(sorted(set(text), key=text.index))

def generate_alphabet(key, alphabet):
    key = remove_duplicates(key)
    key += alphabet
    key = remove_duplicates(key)
    return key

def polyalphabetic_cipher(plaintext, key, alphabet):
    ciphertext = ''
    key = generate_alphabet(key, alphabet)
    
    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += key[index]
        else:
            ciphertext += char
    
    return ciphertext

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key1 = 'merdeka'
    key2 = 'indonesia'
    plaintext = 'belajar kriptografi'
    hasil = key1 + alphabet

    plaintext = plaintext.lower()
    ciphertext = polyalphabetic_cipher(plaintext, key1, alphabet)

    # Tambahkan kunci silang
    key2 = generate_alphabet(key2, alphabet)
    ciphertext_with_cross_key = polyalphabetic_cipher(ciphertext, key2, alphabet)

    result = " ".join(dict.fromkeys(hasil))
    print(result)
    print(f'Plaintext  : {plaintext}')
    print(f'Kunci 1      : {key1}')
    print(f'Kunci 2      : {key2}')
    print(f'Ciphertext : {ciphertext_with_cross_key.upper()}')

if __name__ == '__main__':
    main()
