import itertools

a = {1,2,3,4}
res = []

for i in range(1,len(a)+1):
    res.append([])
    for b in itertools.combinations(a,i):
        res[i-1].append(set(b))

print(res)