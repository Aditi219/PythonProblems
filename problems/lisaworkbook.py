def workbook(n, k, arr):
    total = 0
    count = 0
    for i in range(n):
        if arr[i] % k == 0:
            page = arr[i]//k
        else:
            page = arr[i]//k+1
        p = total+1
        if arr[i] > total:
            element = 1
            for j in range(p, page+total+1):
                x = 1
                while x <= k and element <= arr[i]:
                    if element == j:
                        count += 1
                    element += 1
                    x += 1
        total += page
    return count
