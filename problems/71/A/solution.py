# Write your solution here
def solve() -> None:
    n = int(input())
    for _i in range(0,n):
        s = str(input())
        l = len(s)
        if l > 10:
            print(f"{s[0]}{l - 2}{s[l - 1]}")
        else:
            print(s)


if __name__=="__main__":
    solve()