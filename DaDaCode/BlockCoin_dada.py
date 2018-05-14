#-*- coding:utf-8 -*-
#Filename:BlockCoin_dada.py
#Date    :2018/5/14 下午2:13
#auther  :mudy
#E-mail  :2808050775@qq.com
#Blog    :txmudy.cn

from Block import Block, InvalidBlock
from Transtion import Transaction
from Message import DaDaMessage


class DaDa_BlockCoin:
    def __init__(self):
        self.blockList = []#装载所有的区块

    def validate(self):#校验
        for i ,block in enumerate(self.blockList):
            try:
                block.validate()
            except InvalidBlock as e:
                raise InvalidBlockCoin("区块校验错误")

    def add_blobk(self,block):#增加区块
        if len(self.blockList) > 0:
            block.pre_hash = self.blockList[-1].hash
        block.seal()
        block.validate()
        self.blockList.append(block)#增加区块

    def __repr__(self):#字符串格式化
        return "DaDa_区块链:{}".format(len(self.blockList))#


class InvalidBlockCoin(Exception):#异常
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)




if __name__ == "__main__":
    t1 = Transaction("mudy", "xiaoming", 11000)
    t2 = Transaction("mudy2", "xiaoming2", 12000)
    t3 = Transaction("mudy3", "xiaoming3", 13000)
    t4 = Transaction("mudy4", "xiaoming4", 14000)
    t5 = Transaction("mudy5", "xiaoming5", 15000)
    t6 = Transaction("mudy6", "xiaoming6", 15000)
    t7 = Transaction("mudy7", "xiaoming7", 16000)
    t8 = Transaction("mudy8", "xiaoming8", 17000)

    m1 = DaDaMessage(t1)
    m2 = DaDaMessage(t2)
    m3 = DaDaMessage(t3)
    m4 = DaDaMessage(t4)
    m5 = DaDaMessage(t5)
    m6 = DaDaMessage(t6)
    m7 = DaDaMessage(t7)
    m8 = DaDaMessage(t8)

    b1 = Block(m1, m2)
    b2 = Block(m3, m4)
    b3 = Block(m5, m6)
    b4 = Block(m7, m8)

    # m1.data = "dde"

    dada = DaDa_BlockCoin()
    dada.add_blobk(m1)
    dada.add_blobk(m2)
    dada.add_blobk(m3)
    dada.add_blobk(m4)
    print(dada)