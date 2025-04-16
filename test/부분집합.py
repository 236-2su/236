arr = ['Luffy', 'Zoro', 'Sanji']
path = []

def dfs(lev):
    if lev == 3:
        print(*path)
        return
    path.append(arr[lev])
    dfs(lev+1)
    path.pop()
    dfs(lev + 1)
dfs(0)