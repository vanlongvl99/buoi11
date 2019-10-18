import math

class locate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return

if __name__ == "__main__":
    N = int(input())
    for index in range(N):
        n = int(input())
        graph = []
        for i in range(n):
            x, y = map(int, input().split())
            graph.append(locate(x, y)) 
        INF = 1e9
        dist = [[INF for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                a = math.sqrt((graph[i].x - graph[j].x)**2 + (graph[i].y - graph[j].y)**2)
                if a <= 10:
                    dist[i][j] = a
                    dist[j][i] = a
        for i in range(n):
            dist[i][i] = 0
        floyd(n, dist)
        res = 0
        for i in range(n):
            res = max(max(dist[i]),res)
        print("Case #" + str(index + 1) + ":")
        if res != INF:
            print("{:.4f}".format(res))
        else:
            print("Send Kurdy")
        print("")

