#https://codeforces.com/problemset/problem/1/A
def theatreSquare():
    m, n, a = map(int, input().split())
    if m%a==0 :
        val=m//a
    else:
        val=m//a+1
    if n%a==0 :
        val2=n//a
    else:
        val2=n//a+1

    num= val*val2

    print(num)
theatreSquare()