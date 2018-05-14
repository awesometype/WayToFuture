#-*- coding:utf-8 -*-
#Filename:Message.py
#Date    :2018/5/14 下午2:12
#auther  :mudy
#E-mail  :2808050775@qq.com
#Blog    :txmudy.cn

'''
关于交易信息
'''
import datetime,hashlib

class DaDaMessage:#交易记录类
    def __init__(self, data): #初始化
        self.hash = None #表示自身的哈希
        self.pre_hash = None #表示上一个信息记录的哈希
        self.timeStamp = datetime.datetime.now() #交易时间
        self.data = data #表示交易数据
        self.payload_hash = self._hash_payload() #交易后的哈希

    def _hash_payload(self):#对于交易时间和交易数据进行哈希运算
        return  hashlib.sha512((str(self.timeStamp) + str(self.data)).encode("utf-8")).hexdigest() #取得数据的哈希

    def _hash_message(self):#把交易锁定，防篡改的机制
        return hashlib.sha512((str(self.pre_hash) + str(self.payload_hash)).encode("utf-8")).hexdigest()

    def seal(self):#密封
        self.hash = self._hash_message()#锁定对应数据

    def validate(self):#验证
        if self.payload_hash != self._hash_payload():#判断是不是有人修改了
            raise InvalidMessage("交易数据与时间被修改")

        if self.hash != self._hash_message():#判断消息链是不是被修改了
            raise InvalidMessage("交易的哈希连接被修改")

    def __repr__(self):#返回对象的基本信息
        mystr = "hash:{},prev_hash:{},data:{}".format(self.hash,self.pre_hash,self.data)
        return mystr

    def link(self,Message):#
        # print(Message)
        self.pre_hash = Message.hash;#链接的作用，

class InvalidMessage(Exception):#异常
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    try:
        m1 = DaDaMessage("母东永给小明的十个币")
        m2 = DaDaMessage("母东永给小李的十一个币")
        m3 = DaDaMessage("母东永给小张的十二个币")

        m1.seal()
        m2.link(m1)
        m2.seal()
        m3.link(m2)  # 链接
        m3.seal()#交易记录密封

        #修改数据
        m2.data = "数据被修改了"
        m2.hash = "hash也被修改了"

        print(m1)
        print(m2)
        print(m3)

        m1.validate()
        m2.validate()
        m3.validate()#校验
    except InvalidMessage as e:
        print(e)
