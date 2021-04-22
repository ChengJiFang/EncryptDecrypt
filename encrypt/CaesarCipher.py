
"""
凯撒加密与解密

"""
class CaesarCipher(object):
    """
    字符加密解密核心计算
    """
    def __crypt(self,char,key):
        if not char.isalpha():
            return char
        else:
            base = "A" if char.isupper() else "a"
            return chr((ord(char)-ord(base)+key)%26+ord(base))
    # 对字符加密
    def encrty(self,char,key):
        return self.__crypt(char=char,key=key)
    # 对字符解密
    def decrty(self,char,key):
        return self.__crypt(char=char,key=-key)
    """
    文本加密与解密核心算法
    text:待加密或解密文本
    key:偏移量
    func:加密或解密处理函数
    """
    def __crypt_text(self,text,key,func):
        lines = []
        for line in text.split('\n'):
            words = []
            for word in line.split(' '):
                chars = []
                for char in word:
                    chars.append(func(char=char,key=key))
                words.append("".join(chars))
            lines.append(" ".join(words))
        return "\n".join(lines)

    def encrty_text(self,text,key):
        return self.__crypt_text(text=text,key=key,func=self.encrty)

    def decrty_text(self,text,key):
        return self.__crypt_text(text=text,key=key,func=self.decrty)

if __name__ == '__main__':
    plain = """
    you know? I love you!
    """
    key = 3

    cipher = CaesarCipher()

    encrty_text = cipher.encrty_text(text=plain,key=key)
    # 加密
    print('密文：',encrty_text)
    # brx nqrz? L oryh brx!

    decrty_text = cipher.decrty_text(text=encrty_text,key=key)
    # 解密
    print('明文：',decrty_text)
    # you know? I love you!
