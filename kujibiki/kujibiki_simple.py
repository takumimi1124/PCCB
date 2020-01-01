N, M = map(int, input().split())

k_list = []
k_list.append(0)
for i in range(N):
  k_list.append(int(input()))

max_value = 0

for i in range(N):
  for j in range(N):
    for k in range(N):
      for l in range(N):
        tmp_value = k_list[i] + k_list[j] + k_list[k] + k_list[l]
        if (tmp_value >= max_value) & (tmp_value <= M):
          max_value = tmp_value

print(max_value)