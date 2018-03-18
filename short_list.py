s=[1,3,4,8,13,17,20]
x = list(zip(s[0:], s[1:]))
x.sort(key=lambda x: x[1]-x[0])
print(x[0])



