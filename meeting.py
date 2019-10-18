
class street:
    def __init__(self, age, start, stop, energy):
        self.age = age
        self.start = start
        self.stop = stop
        self.energy = energy

def floyd(dist):
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return
if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        INF = 1e9
        distY = [[INF for _ in range(26)] for _ in range(26)]
        distM = [[INF for _ in range(26)] for _ in range(26)]
        for _ in range(n):
            arr = list((input().split()))
            if arr[0] == "Y":
                distY[ord(arr[2]) - 65][ord(arr[3]) - 65] =min(int(arr[4]), distY[ord(arr[2]) - 65][ord(arr[3]) - 65])
                if arr[1] == "B":
                    distY[ord(arr[3]) - 65][ord(arr[2]) - 65] =min(int(arr[4]), distY[ord(arr[3]) - 65][ord(arr[2]) - 65])
            else:
                distM[ord(arr[2]) - 65][ord(arr[3]) - 65] =min(int(arr[4]), distM[ord(arr[2]) - 65][ord(arr[3]) - 65])
                if arr[1] == "B":
                    distM[ord(arr[3]) - 65][ord(arr[2]) - 65] = min(int(arr[4]), distM[ord(arr[3]) - 65][ord(arr[2]) - 65])
        for i in range(26):
            distM[i][i] = 0
            distY[i][i] = 0
        a, b = (input().split())
        floyd(distY)
        floyd(distM)
        res = INF
        stop = ""
        for i in range(26):
            if distY[ord(a) - 65][i] + distM[ord(b) - 65][i] < res:
                res = distY[ord(a) - 65][i] + distM[ord(b) - 65][i]
                stop = chr(i + 65)
        if res < INF:
            print(res, stop)
        else:
            print("You will never meet.")
