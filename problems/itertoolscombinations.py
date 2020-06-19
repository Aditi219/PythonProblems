from itertools import combinations
if __name__=='__main__':
    tup=()
    n=int(input())
    l1=input().split()
    k=int(input())
    p=0
    t=list(combinations(range(1,n+1),k))
    for i in range(len(t)):
        s=t[i]
        for m in range(k):
                if l1[s[m]-1]=='a':
                    p+=1
                    break
    print("%3f"%(p/len(t)))
    