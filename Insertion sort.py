#https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    for i in range(n):
        current=arr[i]
        
        j=i-1
        while (j>=0 and arr[j]>current):
            arr[j+1]=arr[j];
            j=j-1;
            print(arr)
        arr[j+1]=current
        
    print(arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
