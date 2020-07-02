def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def prodl(a):
    result = 1
    for i in a:
        result *= i
    return result


def find_lcm(g1, a1, l1):
    for i in range(2, len(a1)):
        if l1 == a1[i]:
            continue
        else:
            l1 = ((l1)*a1[i])//g1
    return l1


def getTotalX(a, b):
    count = 0
    if len(a) == 1:
        lcm = a[0]
    else:
        num1 = a[0]
        num2 = a[1]
        gcd = find_gcd(num1, num2)
        for i in range(2, len(a)):
            gcd = find_gcd(gcd, a[i])
        lcm = (num1*num2)//gcd
        lcm = find_lcm(gcd, a, lcm)
    if len(b) == 1:
        gcd = b[0]
    else:
        num1 = b[0]
        num2 = b[1]
        gcd = find_gcd(num1, num2)
        for i in range(2, len(b)):
            gcd = find_gcd(gcd, b[i])

    for i in range(min(a), max(b)+1):
        if i % lcm == 0 and gcd % i == 0:
            count += 1
    return count


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)
