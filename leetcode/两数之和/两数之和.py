def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    a = []
    for k, v in enumerate(nums):
        for k_n, v_n in enumerate(nums):
            if v + v_n == target:
                a.append([k,k_n])
    if len(a) !=1:
        for i in a:
            if i[0] != i[1]:
                return i
    else:
        return a[0]


a = [3, 2, 4]

if __name__ == '__main__':
    print(twoSum(a,6))
