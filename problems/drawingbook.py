def pageCount(n, p):
    k=0
    l=0
    for i in range(1,p,2):
        k+=1
    if n%2:
        for j in range(n,p+1,-2):
            l+=1
    else:
        for j in range(n,p,-2):
            l+=1
    if(k<l):
        return(k)
    else:
        return(l)    

if __name__ == "__main__":
    n=int(input())
    p=int(input())
    print(pageCount(n,p))