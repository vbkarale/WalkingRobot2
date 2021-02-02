x = int(input("Enter x position "))
y = int(input("Enter Y position "))
d = input("Enter direction ")
d = d.upper()
s = input("Enter walking String ")
s = s.upper()
pt = 0

length = len(s)


for i in range(length):
    if d == "SOUTH":
        if s[i] == "L":
            d = "EAST"
        elif s[i] == "R":
            d = "WEST"
        elif s[i] == "W":
            pt = int(s[1+i])
            y = y-pt
    elif d == "NORTH":
        if s[i] == "L":
            d = "WEST"
        elif s[i] == "R":
            d = "EAST"
        elif s[i] == "W":
            pt = int(s[1+i])
            y = y+pt
    elif d == "EAST":
        if s[i] == "L":
            d = "NORTH"
        elif s[i] == "R":
            d = "SOUTH"
        elif s[i] == "W":
            pt = int(s[1+i])
            x = x+pt
    elif d == "WEST":
        if s[i] == "L":
            d = "SOUTH"
        elif s[i] == "R":
            d = "NORTH"
        elif s[i] == "W":
            pt = int(s[1+i])
            x = x-pt

print(x,"",y,"",d)
