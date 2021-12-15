
# https://codeforces.com/problemset/problem/50/A

(i,j) = [int(j) for j in input().split()]

if i%2!=0 and j%2!=0:
    dom = ((i-1)//2)*j + (j-1)//2
    print(dom)

elif i%2==0:
    dom = (i//2)*j
    print(dom)

elif j%2==0:
    dom = (j//2)*i
    print(dom)
