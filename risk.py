
def floyd(dist):
    for k in range(1, 21):
        for i in range(1, 21):
            for j in range(1, 21):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return
if __name__ == "__main__":
    index = 1
    while True:
        INF = 1e9
        dist = [[INF for _ in range(21)] for _ in range(21)]
        for i in range(19):
            arr = list(map(int, input().split()))
            if len(arr) != 1:
                for j in range(1, len(arr)):
                    dist[i + 1][arr[j]] = 1
                    dist[arr[j]][i + 1] = 1
        for i in range(21):
            dist[i][i] = 0
        floyd(dist)
        n = int(input())
        print("Test Set #" + str(index))
        for i in range(n):
            res = ""
            a, b = input().split()
            if len(a) == 1:
                res = res + " " + a + " to "
            else:
                res = a + " to "
            if len(b) == 1:
                res = res + " " + b + ":"
            else:
                res = res + b + ":"
            print(res, dist[int(a)][int(b)])
        print("")
        index += 1
    