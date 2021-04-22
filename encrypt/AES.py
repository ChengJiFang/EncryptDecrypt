"""
AES加密与解密
"""
from Crypto.Cipher import AES
import base64

class aes(object):
    def __init__(self):
        self.encrypt_key = "EpSxImA0vpMUAabsjJ"
        self.key = base64.b64decode(self.encrypt_key)

    # 加密
    def encrypt(self,data):
        BS=16
        pad = lambda s:s+(BS-len(s)%BS)*chr(BS-len(s)%BS)
        cipher = AES.new(self.key,AES.MODE_ECB)
        encrypt_data = cipher.encrypt(pad(data))
        return encrypt_data

    # 解密
    def decrypt(self,encrypt_data):
        unpad = lambda s:s[0:-s[-1]]
        cipher = AES.new(self.key,AES.MODE_ECB)
        decrypt_data = unpad(cipher.decrypt(encrypt_data))
        return decrypt_data.decode('utf-8')