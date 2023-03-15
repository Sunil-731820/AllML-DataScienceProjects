
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if (num>max_num):
            num = max_num
    return max_num

max = find_max(120)
print(max)
