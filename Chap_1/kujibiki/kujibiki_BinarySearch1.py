def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == mid:
      return mid
    elif guess > item:
      high = mid - 1
    else:
      low = mid + 1
  
  if list[high] < item:
    return list[high]
  else:
    return list[high - 1]


N, M = map(int, input().split())

k_list = []
k_list.append(0)
for i in range(N):
  k_list.append(int(input()))

k_list.sort()
max_value = 0

for i in range(N + 1):
  for j in range(N + 1):
    for k in range(N + 1):
      tmp_value = k_list[i] + k_list[j] + k_list[k]
      value_l = binary_search(k_list, M - tmp_value)
      if (max_value <= tmp_value + value_l) & (tmp_value + value_l <= M):
        max_value = tmp_value + value_l

print(max_value)