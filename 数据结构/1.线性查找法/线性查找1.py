arr = [15, 20, 11, 56, 12, 77, 99, 101, 22] #数组列表
def search(arr:list,target:int):
    for k, v in enumerate(arr):
        if v == target:
            return k
    return "-1"

if __name__ == '__main__':
    print(search(arr,12))
