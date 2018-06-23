package main

import (
	"crypto/sha256"
	"strconv"
	"fmt"
)

func main() {

	for i := 0; i< 1000000; i++ {
		data := sha256.Sum256([]byte(strconv.Itoa(i)))

		res := string(data[len(data)-2:])
		if  res == "00"{
			fmt.Printf("%d %s %s\n\n",i,res,data)
		}

	}
}
