from collections import Counter

from ciphers.caesar import decrypt

def crack_caesar(ciphertext: str) -> tuple[int, str]:
    """Взлом шифра Цезаря частотным анализом"""
    most_common = Counter(ciphertext).most_common(1)[0][0]
    key = (ord(most_common) - ord(' ')) % 65536
    return key, decrypt(key, ciphertext)
