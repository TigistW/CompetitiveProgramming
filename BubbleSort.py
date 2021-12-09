#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
def countSwaps(a):
    n=len(a)
    swapcount=0
    for i in range(n):
        for j in range(n-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                swapcount+=1 
    print("Array is sorted in",swapcount,"swaps.")   
    return a            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    a=countSwaps(a)
    print("First Element:",a[0])
    print("Last Element:",a[-1])
