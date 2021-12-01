package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	last, current, counter := 0, 0, 0
	input, err := os.Open("input.txt")

	if err != nil {
		log.Fatal("Could not open file 'input.txt'")
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)
	scanner.Scan()
	last, _ = strconv.Atoi(scanner.Text())

	for scanner.Scan() {
		current, _ = strconv.Atoi(scanner.Text())

		if current > last {
			counter++
		}
		last = current
	}

	log.Println(counter)
}
