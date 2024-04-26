#Calculate the true love in the names
name1 = input()
name2 = input()
point1 = 0
point2 = 0
res = name1 + name2
lowerRes = res.lower()
t = lowerRes.count("t")
r = lowerRes.count("r")
u = lowerRes.count("u")
e = lowerRes.count("e")
point1 = t + r + u + e
l = lowerRes.count("l")
o = lowerRes.count("o")
v = lowerRes.count("v")
e = lowerRes.count("e")
point2 = l + o + v + e
ptr = str(point1) + str(point2)
print(f"Your score is {ptr}")