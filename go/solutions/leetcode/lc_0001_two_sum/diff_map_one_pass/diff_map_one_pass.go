// cspell: ignore diffmaponepass
package diffmaponepass

func twoSum(nums []int, target int) []int {
	diffMap := make(map[int]int)
	for idx, num := range nums {
		complement := target - num
		if complementIdx, ok := diffMap[complement]; ok {
			return []int{complementIdx, idx}
		}
		diffMap[num] = idx
	}
	return []int{}
}

func TwoSum(nums []int, target int) []int {
	return twoSum(nums, target)
}
