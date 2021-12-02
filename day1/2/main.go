package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func sum(slice [3]int) int {
	sum := 0
	for _, e := range slice {
		sum += e
	}
	return sum
}

func exitIfError(err error, msg string) {
	if err != nil {
		log.Fatal("Could not open file 'input.txt'")
		os.Exit(1)
	}
}

func main() {
	var tripel = [3]int{}
	input, err := os.Open("input.txt")

	exitIfError(err, "Could not open file 'input.txt'")

	defer input.Close()
	scanner := bufio.NewScanner(input)

	scanner.Scan()
	tripel[0], err = strconv.Atoi(scanner.Text())
	exitIfError(err, "Unexpected end of file")

	scanner.Scan()
	tripel[1], err = strconv.Atoi(scanner.Text())
	exitIfError(err, "Unexpected end of file")

	scanner.Scan()
	tripel[2], err = strconv.Atoi(scanner.Text())
	exitIfError(err, "Unexpected end of file")

	counter := 0
	for scanner.Scan() {
		sum0 := sum(tripel)
		current, err := strconv.Atoi(scanner.Text())
		exitIfError(err, "Unexpected end of file")
		sum1 := sum0 - tripel[0] + current

		if sum1 > sum0 {
			counter++
		}

		tripel[0] = tripel[1]
		tripel[1] = tripel[2]
		tripel[2] = current
	}

	log.Println(counter)
}
