import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

distances = list(sorted(map(int, input().split())))

diff_dist = [distances[i + 1] - distances[i] for i in range(0, n - 1)]

diff_dist.sort(reverse=True)
diff_dist = diff_dist[k - 1 :]

print(sum(diff_dist))
