#-*- coding:utf-8 -*-
#Filename:Block.py
#Date    :2018/5/14 下午2:13
#auther  :mudy
#E-mail  :2808050775@qq.com
#Blog    :txmudy.cn

'''
包含交易的区块
涉及到
'''


import datetime,hashlib
from Message import DaDaMessage
from Transtion import Transaction

class Block:
    def __init__(self,*args):
        self.messagelist = []#存储多个交易记录
        self.timeStamp = datetime.datetime.now()#存储多个记录最终锁定时间
        self.hash = None #当前的哈希散列
        self.pre_hash = None #上一块的哈希散列

        if args:
            for arg in args:
                self.add_message(arg)

    def add_message(self,message):#增加交易信息
        #区分第一条与后边多条，是否需要链接
        if len(self.messagelist) > 0:
            message.link(self.messagelist[-1])#链接最后一个
        message.seal()#密封
        message.validate()#
        self.messagelist.append(message)#追加记录

    def link(self, block):#链接,将区块链接起来
        self.pre_hash = block.hash

    def seal(self):#密封
        self.timeStamp = datetime.datetime.now()#密封当前时间
        self.hash = self._hash_block() #密封确定当前的哈希值

    def _hash_block(self):
        return hashlib.sha256((str(self.pre_hash) + str(self.timeStamp) + str(self.messagelist[-1].hash)).encode("utf-8")).hexdigest()

    def validate(self):#校验
        for i, message in enumerate(self.messagelist):#每一个交易记录都要校验
            message.validate()
            if i > 0 and message.pre_hash != self.messagelist[i-1].hash:
                 raise InvalidBlock("无效的block，{}交易记录已经被修改了".format(i)+str(self))
        return str(self) + "数据OK"

    def __repr__(self):#描述
        return "money block = hash:{},prehash:{},len:{},time:{},data:{}".format(self.hash,self.pre_hash,len(self.messagelist),self.timeStamp,self.messagelist)


class InvalidBlock(Exception):#异常
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


    b1 = Block(m1,m2,m3,m4)
    b1.seal()
    # m3.data = "我就是被修改的内容" #尝试修改的时候报错

    # b2 = Block(m5, m6, m7)
    # b2.seal()
    # b2.link(b1)
    # b3 = Block(m8)
    # b3.seal()
    # b3.link(b2)
    #
    #
    # print(b1.validate())
    # print(b2.validate())
    print(b1.validate())