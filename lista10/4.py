sums = set()

def one(arr):
    if len(arr) == 0:
        sums.add(0)
    else:
        sums.add(sum(arr))
        for num in arr:
            temp = [x for x in arr if x !=num]
            one(temp)

one([1,2,3,100])
print(set(sorted(sums)))


def two(N, A, B):
    return [[]] if N == 0 else [
        [x] + seq
        for x in range(A, B + 1)
        for seq in two(N - 1, x, B)
    ]

print(two(3,1,5))
