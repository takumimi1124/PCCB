import sys
sys.setrecursionlimit(pow(10, 6))

# 入力
H, W = map(int, input().split())

field_list = [] * H
reached_list = [[0 for i in range(W)] for j in range(H)]
goal_flag = False

for i in range(H):
  field_list.append(list(input()))

# dfs 現在位置は（x, y）
def search(x, y):
  global goal_flag

  # 範囲外に訪れた場合はreturn
  if x < 0 or H <= x or y < 0 or W <= y: return
  # 堀を訪れていればreturn
  if field_list[x][y] == '#': return

  # 訪れたことのある場所であればreturn
  if reached_list[x][y]: return

  # 魚屋に着いたら到着フラグを立てる
  if field_list[x][y] == 'g':
    goal_flag = True
  
  reached_list[x][y] = True

  search(x + 1, y)
  search(x - 1, y)
  search(x, y + 1)
  search(x, y - 1)

# solve
res = 'No'
for i in range(H):
  for j in range(W):
    if field_list[i][j] == 's':
      search(i, j)
      break

if goal_flag:
  print("Yes")
else:
  print("No")