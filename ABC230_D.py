import io
import sys

_INPUT = """\
6
3 3
1 2
4 7
5 9
3 3
1 2
4 7
4 9
5 2
1 100
1 1000000000
101 1000
9982 44353
1000000000 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,D=map(int,input().split())
  wall=[list(map(int,input().split())) for _ in range(N)]
  wall.sort(key=lambda x: x[1])
  ans=0
  idx=0
  while idx<N:
    ans+=1
    now=idx
    while now<N and wall[now][0]<wall[idx][1]+D:
      now+=1
    idx=now
  print(ans)