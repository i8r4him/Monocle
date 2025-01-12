from Crypto.Cipher import AES
from Crypto.Util.Padding  import unpad
from compression import decompress_message

def get_key():
    return bytes.fromhex("546869734973413136427974654b6579")

def decrypt_message(key, combined):
    iv = combined[:AES.block_size]
    cipher_text = combined[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return unpad(cipher.decrypt(cipher_text), AES.block_size)

def simple_substitution_decrypt(substituted_message):
    if substituted_message.startswith("https://_"):
        substituted_message = substituted_message[9:]
    else:
        return "Diese Nachricht ist nicht für dich bestimmt!'"

    reverse_substitution_key = str.maketrans(
        "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza/",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    )
    original_message = substituted_message.translate(reverse_substitution_key)
    return original_message

def main():
    #combined_hex = "e10aedea2a3c17edddc43c764482f7393de448d210e305e81e499666f7d290d651937f20765672a495242bca91a03b2d1bbb55452c1549b73a0548c740ec4b8b"
    #combined = bytes.fromhex(combined_hex)
    substituted_message = "https://_Jo/dbtf/pg/gjsf:/hju/dpnnju,/hju/qvti,/mfbwf/uif/cvjmejoh"

    #key = get_key()
    #decrypted_message = decrypt_message(key, combined)  # Entschlüsseln Sie zuerst
    decrypted_message2 = simple_substitution_decrypt(substituted_message)
    #decompressed_message = decompress_message(decrypted_message)  # Dekomprimieren Sie dann
    
    #print("Dekomprimierte und entschlüsselte Nachricht:", decompressed_message)
    print("Entschlüsselte Nachricht:", decrypted_message2)
    #print("Entschlüsselte Nachricht:", decompressed_message.decode('utf-8'))

if __name__ == "__main__":
    main()
