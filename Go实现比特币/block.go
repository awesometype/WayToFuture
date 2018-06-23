//Filename:block
//Date:2018-06-23 20:45
//auther:Mudy
//E-mail:2808050775@qq.com
//Blog:txmudy.cn
package main

import (
	"strconv"
	"bytes"
	"crypto/sha256"
	"time"
)

type Block struct {
	TimeStamp int64 //时间戳
	Data []byte //交易数据 存储到硬盘文件中
	PrevBlockHash []byte //上一块的哈希
	Hash []byte //当前块的哈希
}

//设定结构体对象的哈希
func (block *Block)SetHash()  {
	//处理当前的时间，转换为10进制的字符串，再转化为字节集
 	timeStamp := []byte(strconv.FormatInt(block.TimeStamp,10))
 	//叠加要哈希的数据
 	headers := bytes.Join([][]byte{block.PrevBlockHash,block.Data,timeStamp},[]byte{})
 	//计算出hash地址
 	hash := sha256.Sum256(headers)
 	block.Hash = hash[:]
}

//创建一个区块
func NewBlock(data string,prevHash []byte)  *Block{

	block := &Block{time.Now().Unix(),[]byte(data),prevHash,[]byte{}}
	block.SetHash()//设置当前块的hash
	return block
}


//创建创世区块
func NewGentBlock() *Block {
	return NewBlock("我是创世区块",nil)
}

