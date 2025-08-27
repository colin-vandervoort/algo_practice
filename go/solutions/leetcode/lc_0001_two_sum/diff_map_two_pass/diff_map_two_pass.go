// cspell: ignore diffmaptwopass
package diffmaptwopass

func twoSum(nums []int, target int) []int {
	diffMap := make(map[int]int)
	for index, num := range nums {
		diffMap[target-num] = index
	}
	for index, num := range nums {
		otherNumIndex, summandsFound := diffMap[num]
		if summandsFound && index != otherNumIndex {
			return []int{index, otherNumIndex}
		}
	}
	return nil
}

func TwoSum(nums []int, target int) []int {
	return twoSum(nums, target)
}
