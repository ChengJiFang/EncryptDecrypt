"""
RSA非对称加密与解密
"""
import rsa

class RSA(object):
    def __init__(self,number,pub_path="public_key.pem",priv_path="private_key.pem"):
        self.public_key,self.private_key = rsa.newkeys(number)
        self.pub_path = pub_path
        self.priv_path = priv_path
    # 获取公钥信息
    def get_public_key(self):
        return self.public_key

    # 获取私钥信息
    def get_private_key(self):
        return self.private_key

    # 存储公钥和私钥
    def key_transform_store(self):
        pub = self.public_key.save_pkcs1('PEM')
        priv = self.private_key.save_pkcs1('PEM')
        with open(self.pub_path,mode='wb') as f:
            f.write(pub)

        with open(self.priv_path,mode='wb') as f:
            f.write(priv)

    # 加密
    def encry(self,info):
        # 读取公钥
        with open(self.pub_path,mode='rb') as f:
            pub = f.read()
            public_key = rsa.PublicKey.load_pkcs1(pub)
        # 加密信息
        info_encryed = rsa.encrypt(info.encode('utf-8'),public_key)
        return info_encryed

    # 解密
    def decry(self,info_encryed):
        # 读取私钥
        with open(self.priv_path,'rb') as f:
            priv = f.read()
            private_key = rsa.PrivateKey.load_pkcs1(priv)
        # 解密信息
        msg = rsa.decrypt(info_encryed,private_key)
        info = msg.decode('utf-8')
        return info

rsa_obj = RSA(1024)  # 实例化
print(rsa_obj.get_public_key())
print(rsa_obj.get_private_key())

