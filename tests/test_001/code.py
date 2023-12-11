def time_by_sec(h,m,s):
    res = s + m * 60 + h * 60 * 60
    return res

def printsec(s):
    d=0
    ss=0
    if(s>0):
        d=int(s/60)
        ss=int(s%60)
    mm=0
    hh=0
    if (d>0):
        mm = int(d%60)
        hh = int(d/60)
    out = ""
    if(hh<10): 
        out += "0"
    out+=str(hh)
    out+=":"
    if(mm<10): 
        out+="0"
    out += str(mm)
    out += ":"
    if(ss<10): 
        out+="0"
    out += str(ss)
    print(out)   

time_str = input()
hours, minutes, seconds = time_str.split(":")
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

al_time_str = input()
al_hours, al_minutes, al_seconds = al_time_str.split(":")
al_hours = int(al_hours)
al_minutes = int(al_minutes)
al_seconds = int(al_seconds)

all_the_day = 24 * 60 * 60
al_by_sec = time_by_sec(al_hours,al_minutes,al_seconds)
t_by_sec = time_by_sec(hours,minutes,seconds)
dif = al_by_sec - t_by_sec
if(dif<=0): 
    dif = al_by_sec + (all_the_day - t_by_sec)
printsec(dif)
