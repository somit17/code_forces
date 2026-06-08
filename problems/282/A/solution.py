# Write your solution here
def solve()->None:
    n = int(input())
    num = 0
    for _i in range(0,n):
        s = str(input())
        if "++" in s:
            num+=1
        else:
            num-=1
    print(num)

if __name__=="__main__":
    solve()