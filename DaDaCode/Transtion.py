#-*- coding:utf-8 -*-
#Filename:Transtion.py
#Date    :2018/5/14 下午3:31
#auther  :mudy
#E-mail  :2808050775@qq.com
#Blog    :txmudy.cn

import datetime

class Transaction:
    def __init__(self,
                 payer,#付款方
                 recer,#收款方
                 money):#钱
        self.payer = payer
        self.recer = recer
        self.money = money
        self.timeStamp = datetime.datetime.now()

    def __repr__(self):#mudypayxiaoming120002018-05-14 15:45:13.220135
        return str(self.payer) + " pay " + str(self.recer) + " " + str(self.money)+ " " + str(self.timeStamp)

    # def __str__(self):   #mudypayxiaoming120002018-05-14 15:46:52.661991
    #     return str(self.payer) + "pay" + str(self.recer) + str(self.money) + str(self.timeStamp)



if __name__ == "__main__":
    t1 = Transaction("mudy","xiaoming",12000)
    print(t1)