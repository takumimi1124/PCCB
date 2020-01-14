# 入力
N,M = map(int, input().split())

field_list = [] * N

for i in range(N):
  field_list.append(list(input()))

# dfs　現在位置（x、y）
def dfs(x, y):
  field_list[x][y] = '.'

  # 移動する８方向をループ
  for dx in range(-1, 3):
    for dy in range(-1, 3):
      # x方向にdx, y方向にdy移動した場所を(nx, ny)とする
      nx = x + dx
      ny = y + dy

      # nxとnyが庭の範囲内かどうかとfield_listが水溜りかどうかを判定
      if 0 <= nx and nx < N and 0 <= ny and ny < M and field_list[nx][ny] == 'W':
        dfs(nx, ny)
  return

# solve
res = 0
for i in range(N):
  for j in range(M):
    if(field_list[i][j] == 'W'):
      # Wが残っているならそこからdfsを始める
      dfs(i, j)
      res += 1

print(res)