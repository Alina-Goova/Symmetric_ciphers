def encrypt(message: str, rounds: int = 16, block_size: int = 8) -> str:
    """Сеть Фейстеля"""
    if len(message) % 2 != 0:
        message += ' '
    
    left, right = message[:len(message)//2], message[len(message)//2:]
    
    for i in range(rounds):
        round_func = lambda x, k: ''.join(chr((ord(c) + k) % 256) for c in x)
        new_right = ''.join(chr(ord(l) ^ ord(r)) for l, r in zip(left, round_func(right, i)))
        left, right = right, new_right
    
    return left + right

def decrypt(ciphertext: str, rounds: int = 16, block_size: int = 8) -> str:
    """Дешифрование Фейстеля"""
    left, right = ciphertext[:len(ciphertext)//2], ciphertext[len(ciphertext)//2:]
    
    for i in reversed(range(rounds)):
        round_func = lambda x, k: ''.join(chr((ord(c) + k) % 256) for c in x)
        old_left = ''.join(chr(ord(r) ^ ord(l)) for l, r in zip(right, round_func(left, i)))
        right, left = left, old_left
    
    return left + right
