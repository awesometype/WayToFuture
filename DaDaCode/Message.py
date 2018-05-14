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
        if self.payload_hash != self._hash_message():#判断是不是有人修改了
            print("交易数据与时间被人修改了")

        if self.hash != self._hash_message():#判断消息链是不是被修改了
            print("交易的哈希连接被修改")

    def __repr__(self):#返回对象的基本信息
        mystr = "hash:{},prev_hash:{},data:{}".format(self.hash,self.pre_hash,self.data)
        return mystr

    def link(self,Message):#
        # print(Message)
        self.pre_hash = Message.hash;#链接的作用，


if __name__ == "__main__":
    m1 = DaDaMessage("母东永给小明的十个币")
    m2 = DaDaMessage("母东永给小李的十一个币")
    m3 = DaDaMessage("母东永给小张的十二个币")

    m1.seal()
    m2.seal()
    m3.seal()

    m2.link(m1)
    m3.link(m2)

    print(m1)
    print(m2)
    print(m3)
'''
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/mudy/Documents/WayToFuture/DaDaCode/Message.py
hash:1174932458a724a606e7fc87a81135a1cb8b1208a6c8257354f76e2bbd85b0665eeeb4696478c3bcf5aefd5cf118e4391e59e8b5db69e022121587fcaec17559,prev_hash:None,data:母东永给小明的十个币
hash:edc12f1ee5bb1942ea447596eb4c07535ddf83069935500ab7c022bd5fbb8d4c85bc08d29d66ac7634ba2680cd1911fde840fd312f314bb5d96562ad7fab354f,prev_hash:1174932458a724a606e7fc87a81135a1cb8b1208a6c8257354f76e2bbd85b0665eeeb4696478c3bcf5aefd5cf118e4391e59e8b5db69e022121587fcaec17559,data:母东永给小李的十一个币
hash:efc1c1928e0e9a73b778ff0bc46e0319e2028aaa06037c888132f44df3ae0efeb76f0d8c57d1f40372c321008baed78d259ef6cc1e3f05bec818bd120807c1fb,prev_hash:edc12f1ee5bb1942ea447596eb4c07535ddf83069935500ab7c022bd5fbb8d4c85bc08d29d66ac7634ba2680cd1911fde840fd312f314bb5d96562ad7fab354f,data:母东永给小张的十二个币
'''