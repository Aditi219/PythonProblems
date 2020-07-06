def saveThePrisoner(n, m, s):
    div=m%n
    if div==0:
        if s>1:
            return s-1
        else:
            return n
    else:
        ans=s+(div-1)
        if ans>n:
            return ans-n
        else:
            return ans
   