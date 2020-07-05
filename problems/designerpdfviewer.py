def designerPdfViewer(h, word):
    length=len(word)
    ans=[]
    for i in range(length):
        ans.append(h[ord(word[i])-97])
    return length*max(ans)