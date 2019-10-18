
class res:
    def __init__(self, index, friends):
        self.index = index
        self.friends = friends

def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        arr = input()
        dist = [[] for i in range(len(arr))]
        INF = 1e9
        for x in arr:
            if x == "N":
                dist[0].append(INF)
            else:
                dist[0].append(1)
        for i in range(1, len(arr)):
            arr1 = input()
            for x in arr1:
                if x == "N":
                    dist[i].append(INF)
                else:
                    dist[i].append(1)
        
        for i in range(len(arr)):
            dist[i][i] = 0
        floyd(len(arr), dist)

        maxFiend = res(0, 0)
        for i in range(len(arr)):
            dem = 0
            for j in range(len(arr)):
                if dist[i][j] == 2:
                    dem += 1
            if dem > maxFiend.friends:
                maxFiend.friends = dem
                maxFiend.index = i
        print(maxFiend.index, maxFiend.friends)
        