//Filename:BlockChain
//Date:2018-06-23 21:08
//auther:Mudy
//E-mail:2808050775@qq.com
//Blog:txmudy.cn
package main

type BlockChain struct {
	blocks []*Block //数组中的每一个约束都是指针，存储区块的地址

}

//增加一个区块
func (blocks *BlockChain) AddBlock(data string) {
	prevBlock := blocks.blocks[len(blocks.blocks)-1]//取出最后一个区块
	newBlock := NewBlock(data,prevBlock.Hash)//根据上一个区块创建一个区块
	blocks.blocks = append(blocks.blocks,newBlock)//区块链插入新的区块

}

//创建一个区块链
func NewBlockChain() *BlockChain  {
	return &BlockChain{[]*Block{NewGentBlock()}}
}


