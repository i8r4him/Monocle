import qrcode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from compression import compress_and_choose_message

class QRCodeGenerator:
    def __init__(self, data: str):
        self.data = data

    def generate_qr_code(self, output_path: str) -> None:
        # Komprimieren und verschlüsseln
        compressed_text = compress_and_choose_message(self.data)
        key = generate_key()
        encrypted_message, iv = encrypt_message(key, compressed_text)

        # QR-Code erstellen und speichern
        qr_code_data = encrypted_message.hex()
        qr_code = qrcode.make(qr_code_data)
        qr_code.save(output_path)

        print("Generierter Schlüssel:", key.hex())
        print("IV:", iv.hex())
        print("Verschlüsselte Nachricht:", encrypted_message.hex())
        print(f"QR Code gespeichert unter {output_path}")

def generate_key():
    return get_random_bytes(16)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = cipher.iv

    return iv + cipher_text, iv