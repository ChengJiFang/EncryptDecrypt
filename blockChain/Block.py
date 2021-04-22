"""
区块设计
"""

import time
import hashlib

class Block:
    # 初始化一个区块
    def __init__(self,previous_hash,data):
        self.index = 0
        self.nonce = ''
        self.previous_hash = previous_hash
        self.time_stamp = time.time()
        self.data = data
        self.hash = self.get_hash()
    # 获取区块的hash
    def get_hash(self):
        msg = hashlib.sha256()
        msg.update(str(self.previous_hash).encode('utf-8'))
        msg.update(str(self.data).encode('utf-8'))
        msg.update(str(self.time_stamp).encode('utf-8'))
        msg.update(str(self.index).encode('utf-8'))
        return msg.hexdigest()
    # 修改区块的hash值
    def set_hash(self,hash):
        self.hash = hash










