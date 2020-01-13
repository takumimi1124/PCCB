# 二分探索を活用した高速化くじ引き問題
# メモリを犠牲に（入力の組合わせ配列を事前に準備する）
# 処理速度を速くする（ループを1つ減らす）

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

## 入力を格納する配列
N, M = map(int, input().split())
k_list = []
k_list.append(0)
for i in range(N):
  k_list.append(int(input()))

## 高速化をするための二重配列を作成
kk_list = []
for i in range(len(k_list)):
  for j in range(len(k_list)):
    kk_list.append(k_list[i] + k_list[j])

## 二分探索の下準備にソートする
kk_list.sort()

## 計算する
max_value = 0
for i in range(N + 1):
  for j in range(N + 1):
    tmp_value = k_list[i] + k_list[j]
    value_l = binary_search(kk_list, M - tmp_value)
    if (max_value <= tmp_value + value_l) & (tmp_value + value_l <= M):
      max_value = tmp_value + value_l

print(max_value)