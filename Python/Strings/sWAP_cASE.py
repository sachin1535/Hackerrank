strIP = input();
res = "";
for c in strIP:
    if c.islower():
        l = c.upper();
    else:
        l= c.lower();
    res = res+l;
print(res);