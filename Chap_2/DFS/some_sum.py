def dfs(i, sum):
  # n個決め終わったら、今まで和のsumがkと等しいかを示す
  if i == n: return sum == k

  # a[i]を使わない場合
  if dfs(i + 1, sum): return True

  # a[i]を使う場合
  if dfs(i + 1, sum + a[i]): return True

  # a[i]を使っても使わなくてもダメな場合Falseを返す
  return False


########################################

n = int(input())
a = list(map(int, input().split()))
k = int(input())

if dfs(0, 0):
  print("Yes")
else:
  print("No")