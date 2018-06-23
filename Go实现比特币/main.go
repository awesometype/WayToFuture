//Filename:main
//Date:2018-06-23 20:45
//auther:Mudy
//E-mail:2808050775@qq.com
//Blog:txmudy.cn
package main

import "fmt"

func main() {
	bc := NewBlockChain()//创建一个区块链
	bc.AddBlock("mudy借给马云8个亿")
	bc.AddBlock("mudy借给马化腾9个亿")
	bc.AddBlock("mudy借给李彦宏10个亿")

	for _,block := range bc.blocks{
		fmt.Printf("上一块哈希%x 数据%s \n",block.PrevBlockHash,block.Data)

	}
	
}
