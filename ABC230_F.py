import io
import sys

_INPUT = """\
6
3
1 -1 1
10
377914575 -275478149 0 -444175904 719654053 -254224494 -123690081 377914575 -254224494 -21253655
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  mod=998244353