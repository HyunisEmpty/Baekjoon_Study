k = int(input())

fibo = [0] * (k + 1)
fibo[1] = 1

for i in range(2, k + 1) :
  fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[k-1], fibo[k])