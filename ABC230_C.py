import io
import sys

_INPUT = """\
6
5 3 2
1 5 1 5
5 3 3
4 5 2 5
1000000000000000000 999999999999999999 999999999999999999
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,A,B=map(int,input().split())
  P,Q,R,S=map(int,input().split())
  ans=[['.']*(S-R+1) for _ in range(Q-P+1)]
  for i in range(Q-P+1):
    for j in range(S-R+1):
      if P+i+R+j==A+B or P+i-R-j==A-B:
        ans[i][j]='#'
  for i in range(Q-P+1):
    print(''.join(ans[i]))