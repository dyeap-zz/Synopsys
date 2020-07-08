# Below is three different function implementations of storing neighbors of sequence
# A - easiest and quickest function to understand solution
# B - fewest number of python line solution
# C - fewest memory usage solution

# A
def easily_understood(nums):
    res = []
    for idx in range(1,len(nums)):
        front_item, prev_item = nums[idx], nums[idx-1]
        pair = (front_item,prev_item)
        res.append(pair)
    return res

# B
def fewest_lines(nums):
    res = []
    for idx in range(1,len(nums)):
        res.append((nums[idx],nums[idx-1]))
    return res

# C
def fewest_memory(nums):
    res = []
    while len(nums) >= 2:
        front_item, prev_item = nums[-1], nums[-2]
        pair = (front_item, prev_item)
        res.insert(0,pair)
        nums.pop()
    return res
