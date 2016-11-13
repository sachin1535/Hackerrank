ip = input()
change  = input().split()
str = list(ip)
str[int(change[0])] = change[1];
print("".join(str))