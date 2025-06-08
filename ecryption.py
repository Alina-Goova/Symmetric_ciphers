def encrypt(key: str, message: str) -> str:
    """Шифр Вернама (XOR)"""
    if len(key) != len(message):
        raise ValueError("Длина ключа должна совпадать с длиной сообщения")
    return ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))

# Для Вернама encrypt и decrypt одинаковы
decrypt = encrypt
