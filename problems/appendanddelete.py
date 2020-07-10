def appendAndDelete(s, t, k):
    if len(s) == len(t):
        min1 = len(s)
        max1 = len(s)
    else:
        min1 = min(len(s), len(t))
        max1 = max(len(s), len(t))
    if len(s)+len(t) <= k:
        return "Yes"
    common_len = 0
    for i in range(min1):
        if s[i] == t[i]:
            common_len += 1
        else:
            break
    if common_len == 0:
        return "No"
    min2 = ((min1-common_len)+(max1-common_len))
    if min2 % 2 == 0:
        if k >= min2 and k % 2 == 0:
            return "Yes"
        else:
            return "No"
    else:
        if k >= min2 and k % 2 != 0:
            return "Yes"
        else:
            return "No"
