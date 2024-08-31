[saldo, N] = [int(x) for x in input().split(" ")]

precos = {} 

for _ in range(N):
    row = input().split(" ")
    key = row[0]
    new = int(row[1])
    if key in precos:
        if new < precos[key]:
            precos[key] = new
    else:
        precos[key] = new


p = list(precos.values())
p.sort()

# print(precos)
# print(p)
# print(saldo)

i = 0
while i < len(p):
    saldo -= p[i]
    if saldo <= 0:
        break
    i += 1

print(i)