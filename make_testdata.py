import random

N = 50
M = 10
k_list = []

for i in range(N):
  k_list.append(random.randint(1, 10))

k_list = map(str, k_list)

file = open('testdata.text', 'w')
file.write(str(N) + " " + str(M) + "\n")
file.writelines(" ".join(k_list))
file.close()