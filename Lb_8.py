from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt_cfb(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def aes_decrypt_cfb(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text

key = get_random_bytes(16)
iv = get_random_bytes(16)

plaintext = b"Hello, this is AES in CFB mode!"

ciphertext = aes_encrypt_cfb(key, iv, plaintext)
print("Encrypted Data:", ciphertext.hex())

decrypted_text = aes_decrypt_cfb(key, iv, ciphertext)
print("Decrypted Data:", decrypted_text.decode())
