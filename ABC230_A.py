import io
import sys

_INPUT = """\
6
42
19
1
50
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=input()
  n=int(N)
  l=len(N)
  if n<42:
    print('AGC'+'0'*(3-l)+str(n))
  else:
    print('AGC'+'0'*(3-l)+str(n+1))