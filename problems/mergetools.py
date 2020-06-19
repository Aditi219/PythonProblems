def merge_the_tools(string, k):
    # your code goes here
    str1=""
    for i in range(len(string)):
        if string[i] not in str1:
            str1=str1+string[i]
        if (i+1)%k==0:
            print(str1)
            str1=""
  
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)