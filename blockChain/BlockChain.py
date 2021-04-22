"""
区块链设计
"""
from Block import *
# 区块链
class BlockChain:
    def __init__(self):
        self.blocks = [creat_genesis_block()]
    # 添加区块到区块链上
    def add_block(self,data):
        pre_block = self.blocks[len(self.blocks)-1]
        new_block = Block(pre_block.hash,data)
        new_block.index = len(self.blocks)
        nonce,digest = mime(block=new_block)
        new_block.nonce = nonce
        new_block.set_hash(digest)
        self.blocks.append(new_block)
        return new_block

# 生成创世区块，这是第一个区块，没有前一个区块
def creat_genesis_block():
    block = Block(previous_hash= '0000',data='Genesis block')
    nonce,digest = mime(block=block)
    block.nonce = nonce
    block.set_hash(digest)
    return block

def mime(block):
    """
    挖矿函数——更新区块结构，加入nonce值
        block:挖矿区块
    """
    i = 0
    prefix = '0000'
    while True:
        nonce = str(i)
        msg = hashlib.sha256()
        msg.update(str(block.previous_hash).encode('utf-8'))
        msg.update(str(block.data).encode('utf-8'))
        msg.update(str(block.time_stamp).encode('utf-8'))
        msg.update(str(block.index).encode('utf-8'))
        msg.update(nonce.encode('utf-8'))
        digest = msg.hexdigest()
        if digest.startswith(prefix):
            return nonce,digest
        i+=1