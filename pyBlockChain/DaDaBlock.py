#-*- coding:utf-8 -*-
#@Filename:DaDaBlock
#@Date:2018-05-10 21:03
#@auther:Mudy
#@E-mail:2808050775@qq.com
#@Blog:txmudy.cn

import hashlib
from datetime import datetime

class DaDaBlock:
    def __init__(self,index,#编号索引
                 timeStamp,#时间戳
                 txData,#交易数据
                 nextHash):#后一个区块的hash 注意的是当前块的hash值是自己计算出来的，还有nextHash是创建下一个区块的时候才会根据其交易的数据产生
        self.timeStamp = timeStamp
        self.index = index;
        self.txData = txData;
        self.nextHash = nextHash;#
        self.currentHash = self.getCurrentHash()

    def getCurrentHash(self):
        txString = str(self.timeStamp) + str(self.txData)
        sha = hashlib.md5()
        sha.update(txString.encode("utf-8"))
        self.curHash = sha.hexdigest()


def createFirstBlock():
    firstBlock = DaDaBlock(0,datetime.now(),"第一个交易信息","0")
    return firstBlock


#创建非首区块
def createBlock(preBlock:DaDaBlock):

    currentTime = datetime.now()
    txString = str(currentTime) + str("交易信息") + str(preBlock.index + 1)
    curBlock = DaDaBlock(preBlock.index + 1, currentTime, txString, preBlock.curHash)
    return curBlock




fb = createFirstBlock()
print(fb.curHash,fb.nextHash)
blocks = []

blocks.append(fb)


for i in range(100):

    block = createBlock(fb)
    fb = block
    print(fb.curHash,fb.nextHash)
