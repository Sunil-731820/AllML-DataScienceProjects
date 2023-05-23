
def find_max(nums):
    print("Finding The Maximum Numbers ")
    max_num = float("-inf")
    for num in nums:
        if (num>max_num):
            num = max_num
    return max_num

# max = find_max(120)

print("The maximum values is ")
print(max)

