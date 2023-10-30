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
    key = 'merdeka'
    plaintext = 'belajar kriptografi'
    hasil = key + alphabet

    plaintext = plaintext.lower()
    ciphertext = polyalphabetic_cipher(plaintext, key, alphabet)
    result = " ".join(dict.fromkeys(hasil))  # Hapus karakter yang sama
    print(result)
    print(f'Plaintext  : {plaintext}')
    print(f'Kunci       : {key}')
    print(f'Ciphertext : {ciphertext.upper()}')
    

if __name__ == '__main__':
    main()