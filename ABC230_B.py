import io
import sys

_INPUT = """\
6
xoxxoxxo
xxoxxoxo
ox
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  if 'oo' in S or 'xxx' in S or 'oxo' in S:
    print('No')
  else:
    print('Yes')