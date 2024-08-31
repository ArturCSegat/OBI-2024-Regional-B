# def get_notation(i, j, k):
#     a = [i, j, k]
#     a.sort()
#     return "".join([str(f) for f in a])

N = int(input())
palitos = [int(x) for x in input().split(" ")]
palitos.sort(reverse=True)
count = 0

for i in range (N):
    for j in range(i+1, N):
        last = count
        for k in range(j+1, N):
            a = palitos[i]
            b = palitos[j]
            c = palitos[k]

            if b+c > a:
                # print(f"{a} {b} {c}")
                count +=1
        if count == last:
            continue
print(count)
