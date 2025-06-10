# two sum
nums = [3, 2, 4, 7, 5, 1]
target = 9

seen = {}
def two_sum(nums, target):
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# 下面會有問題，先將 list set() 會導致順序跳掉，找不到index
# aa = set(nums)
# def two_sum(nums, target):
#     for n in aa:
#         if target-n in aa:
#             return [n,target-n]

# two_sum(nums, target)

# ------------------------------------------------------------------------
# three sum
nums = [-4, -1, -1, 0, 1, 2]
target = 0
def three_sum(nums, target):
    nums.sort()
    left, right = 0, len(nums)-1
    for n in nums[1:-1]:
        while left < len(nums) and right >0:
            temp = nums[left] + n + nums[right]
            if  temp == target:
                print([nums[left], n, nums[right]])
                return [nums[left], n, nums[right]]
            else:
                if temp > target:
                    right -=1
                else:
                    left +=1
        return 0

three_sum(nums, target)

