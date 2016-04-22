package main

import (
	"fmt"
	"math/big"
)


func main() {

	r := big.NewInt(0);
	var i int64;
	for i = 1; i <= 1000; i++ {
		b_i := big.NewInt(i)
		b_i.Exp(b_i, b_i, nil)
		r.Add(r, b_i)
	}
	sr := r.String()
	fmt.Println(sr[len(sr)-10:])
}
