def timeConversion(s):
    hour=s[0:2]
    minute=s[3:5]
    seconds=s[6:8]
    check=s[8:]
    if check =='AM':
        if hour=='12':
            return ('00'+':'+minute+':'+seconds)
        else:
            return s[0:8]
        
    else:
        if hour=='12':
            return s[0:8]
        if hour>='1' or hour<'12':
            temp=int(hour)+12
            return (f"{temp}:{minute}:{seconds}")
    