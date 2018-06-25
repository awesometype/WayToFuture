package main

import (
	"crypto/sha256"
	"strconv"
	"fmt"
	"time"
)

func main1() {

	for i := 0; i< 100000000; i++ {
		data := sha256.Sum256([]byte(strconv.Itoa(i)))
		start := time.Now()
		res := string(data[len(data)-3:])
		if  res == "000"{
			timeUsed := time.Since(start) //挖矿用时
			fmt.Printf("%d %s %s\n\n",i,res,data)
			fmt.Println(timeUsed)
		}

	}
}
