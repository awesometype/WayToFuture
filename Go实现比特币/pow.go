package main

import (
	"math"
	"math/big"
	"bytes"
	"crypto/sha256"
	"fmt"
)

var (
	maxNonce = math.MaxInt64//最大的整数
)

const targetBits  = 24

type ProofOfWork struct {
	block *Block
	target *big.Int //存储特定哈希值的整数
} 

//创建一个工作量证明的挖矿对象
func NewProofOfWork(block *Block) *ProofOfWork  {
	target := big.NewInt(1)//初始化目标整数
	target.Lsh(target,uint(256-targetBits))//数据转换
	pow := &ProofOfWork{block,target}
	return pow
}

//准备数据进行挖矿计算
func (pow *ProofOfWork)prepareData(nonce int)[]byte {
	data := bytes.Join(
		[][]byte{
			pow.block.PrevBlockHash,//上一块哈希
			pow.block.Data,//当前数据
			IntToHex(pow.block.TimeStamp),//时间 十六进制
			IntToHex(int64(targetBits)),//位数 十六进制
			IntToHex(int64(nonce)),//保存工作量的nonce
		},[]byte{},
	)
	return data
}

//挖矿执行的过程
func (pow *ProofOfWork)run()(int,[]byte){
	var hashInt big.Int
	var hash [32]byte
	nonce := 0
	for nonce < maxNonce{
		data := pow.prepareData(nonce)//准备好的数据
		hash = sha256.Sum256(data)//计算出哈希
		fmt.Printf("\r--- %x",hash)//打印显示哈希
		hashInt.SetBytes(hash[:])//获取要对比的数据
		if hashInt.Cmp(pow.target) == -1{//挖矿的校验
			break
		}else {
			nonce ++
		}

	}
	fmt.Println()
	return nonce,hash[:]
}

//校验挖矿是不是真的成功
func (pow *ProofOfWork)Validate() bool{
	var hashInt big.Int
	data := pow.prepareData(pow.block.Nonce)//准备好的数据
	hash := sha256.Sum256(data)//计算哈希
	hashInt.SetBytes(hash[:])//获取要对比的数据
	isValid := (hashInt.Cmp(pow.target)==-1)//校验数据
	return isValid
}