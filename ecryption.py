def encrypt(k: int, m: str) -> str:
    """Шифрование Цезаря с модулем 65536"""
    return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

def decrypt(k: int, c: str) -> str:
    """Дешифрование Цезаря"""
    return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))
