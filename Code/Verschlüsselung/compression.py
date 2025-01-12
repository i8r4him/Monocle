import zlib

def compress_message(message):
    return zlib.compress(message.encode('utf-8'))

def decompress_message(compressed_message):
    try:
        return zlib.decompress(compressed_message).decode('utf-8')
    except zlib.error:
        return compressed_message.decode('utf-8')
    
def compress_and_choose_message(message):
    compressed_message = compress_message(message)
    original_size = len(message.encode('utf-8'))
    compressed_size = len(compressed_message)
    compression_ratio = (1 - compressed_size / original_size) * 100

    #Ausgabe der Infos
    print("Größe der ursprünglichen Nachricht:", original_size, "Bytes")
    print("Größe der komprimierten Nachricht:", compressed_size, "Bytes")
    print("Kompressionsrate: {:.2f}%".format(compression_ratio))

    # Entscheide, welche Nachricht zurückgegeben wird
    if compressed_size < original_size:
        print("Die komprimierte Nachricht wird verwendet.")
        return compressed_message
    else:
        print("Die ursprüngliche Nachricht wird verwendet.")
        return message.encode('utf-8')
        