def migratoryBirds(arr):
    d1={}
    for i in arr:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    d2={}
    for key in d1:
        if d1[key] in d2:
            if d2[d1[key]]>key:
                d2[d1[key]]=key
            else:
                pass
        else:
            d2[d1[key]]=key
    d3=sorted(d2,reverse=True)
  