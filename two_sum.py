
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return target


def solution_2(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        s = target - nums[i]
        if s in hashmap and hashmap[s] != i:
            return [i, hashmap[s]]


