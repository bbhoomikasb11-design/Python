nums = [ 2, 7, 11, 15]
target = 26
n = len(nums)

def twosum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [nums[i],nums[j]]
print(twosum(nums,target))               

