from os import urandom
from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify

hexkey = '140b41b22a29beb4061bda66b6747e14'
CBCCipherhe = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
IVCipherhex = CBCCipherhe[:32]
Cipherhex = CBCCipherhe[32:]
Cipherhex = unhexlify(Cipherhex)
IVCipherhex = unhexlify(IVCipherhex)
hexkey = unhexlify(hexkey)




# For Generating cipher text

obj = AES.new(hexkey, AES.MODE_CBC, IVCipherhex)


# Decrypt the message
rev_obj = AES.new(hexkey, AES.MODE_CBC, IVCipherhex)
decrypted_text = rev_obj.decrypt(Cipherhex)
print(decrypted_text)
