package main

import (
	"fmt"
	"strconv"
	"strings"
)

// dfs, probably O(n^2)
func decodeString(s string) string {
	if s == "" {
		return s
	}
	repeat := 0
	expr_start := -1
	last_expr_end := -1
	opened := 0

	res := make([]string, 0)
	for pos, char := range s {
		digit, err := strconv.Atoi(string(char))
		if err == nil {
			if expr_start == -1 {
				repeat *= 10
				repeat += digit
			}
		} else {
			if char != '[' && char != ']' && opened == 0 {
				res = append(res, string(char))
			}
			if char == '[' {
				opened += 1
				if expr_start == -1 {
					expr_start = pos + 1
				}
			}
			if char == ']' {
				opened -= 1
				if opened == 0 {
					substring := decodeString(s[expr_start:pos])
					res = append(res, strings.Repeat(substring, repeat))
					repeat = 0
					expr_start = -1
					last_expr_end = pos
				}
			}
		}
	}

	if last_expr_end+1 < len(s) {
		res = append(res, s[last_expr_end+1:])
	}

	// this is probably O(n^2) since
	// the join happens repeatadly on the same strings
	return strings.Join(res, "")
}

func main() {
	fmt.Println(decodeString("") == "")
	fmt.Println(decodeString("a") == "a")
	fmt.Println(decodeString("aaa") == "aaa")
	fmt.Println(decodeString("3[a]") == "aaa")
	fmt.Println(decodeString("11[ab]") == "ababababababababababab")
	fmt.Println(decodeString("3[2[a]]") == "aaaaaa")
	fmt.Println(decodeString("3[2[ab]]") == "abababababab")
	fmt.Println(decodeString("3[a]2[b]") == "aaabb")
	fmt.Println(decodeString("3[a]2[bc]") == "aaabcbc")
	fmt.Println(decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
	fmt.Println(decodeString("3[a2[c]]") == "accaccacc")
	fmt.Println(decodeString("3[a2[c]]"))
	fmt.Println(decodeString("a2[c]") == "acc")
	fmt.Println(decodeString("a2[c]"))
	fmt.Println(decodeString("a1[c]") == "ac")
	fmt.Println(decodeString("a1[c]"))
}
