
a = [1,2,3,4,5,6,7,7,8,9]
num = 11
start = 0
end = len(a) - 1


def binary_seach(num, start, end):
    while start <= end:
        mid = (start + end) //2
        if a[mid] == num:
            print(num,": number found at location", mid)
            return
        elif a[mid] < num:
            start = mid+1
        else:
            end = mid
    print(num,": Do not exist in list")

binary_seach(num, start, end)
