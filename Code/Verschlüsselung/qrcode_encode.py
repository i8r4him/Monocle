import qrcode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad
from compression import compress_and_choose_message

def generate_key():
    return get_random_bytes(16)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message, AES.block_size))
    iv = cipher.iv

    return iv + cipher_text, iv

def simple_substitution_encrypt(message):
    substitution_key = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ",
        "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza/"
    )
    substituted_message = message.translate(substitution_key)
    return "https://_" + substituted_message

def create_qr_code(data):
    qr_code = qrcode.make(data.hex())
    qr_code.save("verschluesselter_qr_code.png")

def main():  
    plain_text = "Mein C tut W wenn ich T holen G"
    # "My wallet is like an onion, opening it makes me cry"
    # "In case of fire: git commit, git push, leave the building"
    # "Mein C tut W wenn ich T holen G"

    compressed_text = compress_and_choose_message(plain_text)
    #key = generate_key()
    fixed_key = b'ThisIsA16ByteKey'
    encrypted_message, iv = encrypt_message(fixed_key, compressed_text)
    substituted_text = simple_substitution_encrypt(plain_text)

    print("PlainText:",plain_text)
    print("Komprimierte Nachricht:", compressed_text)
    print("Substituted Nachricht:", substituted_text)
    create_qr_code(encrypted_message)

    print("Generierter Schlüssel:", fixed_key.hex())
    print("IV:", iv.hex())
    print("Verschlüsselte Nachricht:", encrypted_message.hex())

if __name__ == "__main__":
    main()

#Ausgeben der Daten
