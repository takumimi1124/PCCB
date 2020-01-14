# 幅優先探索で迷路を進む
# キューに次の行き先を突っ込み、popして進めるか判断していく

from collections import deque

INF = pow(10, 8)

## 入力
N, M = map(int, input().split())
sx, sy = map(int, input().split()) # スタートの座標
gx, gy = map(int, input().split()) #  ゴールの座標
maze = [] * N
for i in range(N):
  maze.append(list(input()))

d = [[INF for i in range(M)] for j in range(N)] # dをINFで初期化

## 移動の４方向ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

## (sx, sy)から(gx, gy)への最短距離を求める
## たどり着けないとINF
def bfs():
  que = deque()
  # スタート地点をqueに入れ、その距離を0とする
  que.append([sx - 1, sy - 1])
  d[sx - 1][sy - 1] = 0

  # queが空になるまでループ
  while len(que):
    # キューの先頭を取り出す
    pop_pair = que.popleft()
    # 取り出してきた状態がゴールなら探索をやめる
    if pop_pair[0] == (gx - 1) and pop_pair[1] == (gy - 1):
      break
    # 移動４方向をループ
    for i in range(4):
      nx = pop_pair[0] + dx[i]
      ny = pop_pair[1] + dy[i]
    # 移動が可能かの判定と既に訪れたことがあるかの判定(d[nx][ny] != INF なら訪れたことがある)
      if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != '#' and d[nx][ny] == INF:
        que.append([nx, ny])
        d[nx][ny] = d[pop_pair[0]][pop_pair[1]] + 1
    
  return d[gx - 1][gy - 1]

## solve
res = bfs()
print(res)




