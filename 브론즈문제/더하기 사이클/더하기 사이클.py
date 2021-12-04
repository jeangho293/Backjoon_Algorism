nums, cycle = input(), 0

if len(nums) == 1:
    nums = '0' + nums
temp = nums
while True:
    first_nums = nums[-1]
    second_nums = str(int(nums[0])+int(nums[1]))
    nums = first_nums + second_nums[-1]
    cycle += 1
    if temp == nums:
        print(cycle)
        break
