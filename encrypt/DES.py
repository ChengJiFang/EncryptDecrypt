"""
DES加密与解密
"""
from Crypto.Cipher import DES

class des(object):
    key = chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11)
    iv = chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22)
    def __init__(self,key="",iv=""):
        if len(key)>0:
            self.key = key
        if len(iv)>0:
            self.iv = iv
    def encrypt(self,encrypt_data):
        try:
            cipherX = DES.new(self.key,DES.MODE_CBC,self.iv)
            pad = 8 - len(encrypt_data) % 8
            padstr = ''
            for i in range(pad):
                padstr = padstr + chr(pad)
            encrypt_data = encrypt_data + padstr
            x = cipherX.encrypt(encrypt_data)
            return x.encode('utf-8').upper()
        except:
            return ""

    def decrypt(self,decrypt_data):
        try:
            cipherX = DES.new(self.key,DES.MODE_CBC,self.iv)
            str = decrypt_data.decode('utf-8')
            y = cipherX.decrypt(str)
            return y[0:ord(y[len(y)-1])*-1]
        except:
            return ""

    if __name__ == '__main__':
        msg = "psw is 123456"
        key = "desdekey"
        des = des(key)
        cipher_data = des.encrypt(encrypt_data=msg)
        print(cipher_data)
        print(des.decrypt(decrypt_data=cipher_data))