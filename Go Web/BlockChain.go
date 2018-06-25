//Filename:BlockChain
//Date:2018-06-21 21:27
//auther:Mudy
//E-mail:2808050775@qq.com
//Blog:txmudy.cn

package main

import (
	"time"
	"crypto/sha256"
	"encoding/hex"
	"github.com/labstack/echo"
	"fmt"
)

type BlockModel struct {
	Id int64 // 索引
	TimeStamp string //区块创建的时间标识
	BPM int //每分钟心跳
	Hash string //区块哈希
	PreHash string//上一块的哈希 sha256
}

//区块链，数组
var BlockChain  = make([]BlockModel,0)

//创建第一个区块，创世区块
func init()  {
	//创建了一个区块
	block := BlockModel{20,time.Now().String(),0,"",""}
	BlockChain = append(BlockChain,block)//加入数组
}

// 哈希处理
func calHash(block BlockModel) string {
	record := string(block.Id) + block.TimeStamp + string(block.BPM) + block.PreHash
	myhash := sha256.New()
	myhash.Write([]byte(record))
	hashed := myhash.Sum(nil)
	return hex.EncodeToString(hashed)//编码为字符串
}

func is_BLockValid(newBlock,lastBlock BlockModel) bool {
	//id不能相等 必须是顺序的
	if lastBlock.Id + 1 != newBlock.Id {
		return false
	}

	//前一块的哈希，不等于新区快的哈希
	if lastBlock.Hash != newBlock.PreHash{
		return false
	}

	if calHash(newBlock) != newBlock.Hash {//数据被修改

	}
	return true
}

//处理区块的创建
func createBlock(ctx echo.Context)  error{
	//处理心跳信息
	type message struct {
		BPM int
	}

	var mymessage = message{}
	if err := ctx.Bind(&mymessage); err != nil{//绑定消息处理
		panic(err)//处理错误
	}
	lastblock := BlockChain[len(BlockChain)-1]//前一个区块
	//使用前一个区块，创建新的区块
	newBlock := BlockModel{}
	newBlock.Id = lastblock.Id + 1
	newBlock.TimeStamp = time.Now().String()
	newBlock.BPM = mymessage.BPM
	newBlock.PreHash = lastblock.Hash
	newBlock.Hash = calHash(newBlock)

	if is_BLockValid(newBlock,lastblock) {
		BlockChain = append(BlockChain,newBlock)
		fmt.Println("创建区块成功",BlockChain[len(BlockChain)-1].Id)
	}else {
		fmt.Println("创建区块失败")
	}

	return ctx.JSON(200,newBlock)
}

func main() {
	echoServer := echo.New()//创建服务器
	echoServer.GET("/", func(context echo.Context) error {
		return context.JSON(200,BlockChain)
	})

	echoServer.POST("/",createBlock)
	echoServer.Logger.Fatal(echoServer.Start(":8800"))
}