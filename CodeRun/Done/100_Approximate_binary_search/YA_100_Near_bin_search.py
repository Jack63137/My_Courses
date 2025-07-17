def binSerach(data,target):
    left_ar = 0
    right_ar = len(data)-1
    if target < data[left_ar]:
        return data[left_ar]  
    if target > data[right_ar]:
        return data[right_ar]
    while left_ar<=right_ar:
        mid=(left_ar+right_ar)//2
        if target==data[mid]:
            return data[mid]
        if left_ar+1 == right_ar:
            if abs(data[right_ar]-target)>=abs(target-data[left_ar]):
                return data[left_ar]
            else:
                return data[right_ar]
        if target>data[mid]:
            left_ar = mid
        if target<data[mid]:
            right_ar = mid
    return print("закончилось")


def main():
    N,K = map(int,input().split())
    mass_n = list(map(int,input().split()))
    mass_k = list(map(int,input().split()))
    for k in mass_k:
        print(binSerach(mass_n,k))


if __name__ == '__main__':
    main()