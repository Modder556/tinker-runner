package main

import "fmt"

func main() {
    fmt.Println("Hello from Go")
    for i := 1; i <= 5; i++ {
        fmt.Printf("%d squared is %d\n", i, i*i)
    }
}
