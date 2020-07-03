def sockMerchant(n, ar):
    dict1={}
    pair=0
    for i in range(n):
        if ar[i] in dict1:
            dict1[ar[i]]+=1
        else:
            dict1[ar[i]]=1
    for key,value in dict1.items():
        if value>1:
                pair+=value//2
    return pair

if __name__ == "__main__":
    n=int(input())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n,ar))