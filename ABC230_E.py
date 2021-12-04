import io
import sys

_INPUT = """\
6
3
10000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=0
  x=0
  while x**2<=N:
    x+=1
  x-=1
  if x*(x+1)<=N:
    for i in range(1,x+1):
      ans+=N//i-x
    ans*=2
    ans+=x**2
  else:
    for i in range(1,x):
      ans+=N//i-x
    ans*=2
    ans+=x**2
  print(ans)