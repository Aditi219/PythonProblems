def minion_game(string):
    # your code goes here
    v=0
    c=0
    s='AEIOU'
    l=len(string)
    for i in range(l):
        if string[i] in s:
            v+=l-i
        else:
            c+=l-i
    if c>v:
        print(f"Stuart {c}")
    elif c<v:
        print(f"Kevin {v}")
    else:
        print("Draw")

            
if __name__ == '__main__':
    s = input()
    minion_game(s)