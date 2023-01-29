a = ['123', '2', 'hdshs', 'ee', '3247942']
b=[]
for i in range(len(a)):
    if len(a[i]) >= 3:
        b.append(a[i])
print(b)