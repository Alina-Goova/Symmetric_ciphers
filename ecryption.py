import os

from ciphers import caesar

def encrypt(key: int, message: str, block_size: int = 16) -> bytes:
    """CBC режим с шифром Цезаря"""
    iv = os.urandom(block_size)
    blocks = [message[i:i+block_size] for i in range(0, len(message), block_size)]
    cipher_blocks = []
    prev_block = iv
    
    for block in blocks:
        xored = ''.join(chr(ord(a) ^ b) for a, b in zip(block, prev_block))
        encrypted = caesar.encrypt(key, xored)
        cipher_blocks.append(encrypted)
        prev_block = [ord(c) for c in encrypted]
    
    return iv + b''.join(bytes(ord(c) for c in ''.join(cipher_blocks)))

def decrypt(key: int, ciphertext: bytes, block_size: int = 16) -> str:
    """Дешифрование CBC"""
    iv = ciphertext[:block_size]
    ciphertext = ciphertext[block_size:]
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    message_blocks = []
    prev_block = iv
    
    for block in blocks:
        decrypted = caesar.decrypt(key, ''.join(chr(b) for b in block))
        xored = ''.join(chr(ord(d) ^ p) for d, p in zip(decrypted, prev_block))
        message_blocks.append(xored)
        prev_block = block
    
    return ''.join(message_blocks)
