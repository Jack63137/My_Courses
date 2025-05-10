mas_count = int(input())
mas = list(map(int,input().split()))
target_val = int(input())
def binSerach(data,target):
    left_ar = 0
    right_ar = len(data)-1
    if target<data[left_ar] or target>data[right_ar]:
        return -1
    while left_ar<=right_ar:
        mid=(left_ar+right_ar)//2
        if target==data[mid]:
            return mid
        if left_ar+1 == right_ar:
            return right_ar
        if target>data[mid]:
            left_ar = mid
        if target<data[mid]:
            right_ar = mid
    return(-1)
        
print(binSerach(data=mas,target=target_val))