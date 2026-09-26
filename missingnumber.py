def missingnumber(nums):
    n = len(nums) #we use this method since there is only one missing number in the range [0, n]
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    nums = [3, 0, 1]
    missing = missingnumber(nums)
    print(f"The missing number is: {missing}")