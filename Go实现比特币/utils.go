package main

import (
	"bytes"
	"encoding/binary"

	"github.com/labstack/gommon/log"
)

//整数转化为十六进制
func IntToHex(num int64) []byte {
	buff := new(bytes.Buffer)
	err := binary.Write(buff,binary.BigEndian,num)
	if err != nil{
		log.Panic(err)
	}

	return buff.Bytes()//返回字节集合
}
//
//func main() {
//	res := IntToHex(3400000)
//	fmt.Println(res)
//}
