import sys


def binSerach(data,target):
    left_ar = 0
    right_ar = len(data)-1
    if target<data[left_ar] or target>data[right_ar]:
        return -1
    while left_ar<=right_ar:
        mid=(left_ar+right_ar)//2
        if target==data[mid]:
            return mid
        if target>data[mid]:
            left_ar = mid +1
        if target<data[mid]:
            right_ar = mid -1
    return -1


def main():
    N,K = map(int,input().split())
    mass_n = list(map(int,input().split()))
    mass_k = list(map(int,input().split()))
    for k in mass_k:
        if binSerach(mass_n,k)!=-1:
            print("YES")
        else:
            print("NO")
        pass


if __name__ == '__main__':
    main()