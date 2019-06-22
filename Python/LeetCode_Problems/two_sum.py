# define a function which accepts two arguments (one is an array and another one is an integer).
# This function will return the integer value. -> means specifying the return type
def twoSum(nums, target) -> int:
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


nums = [2,7, 11, 15]
target = 9
print(twoSum(nums, target))