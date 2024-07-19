import sys
from functools import cache

lines = open(sys.argv[1]).read().splitlines()
res = 0

@cache
def count(str, rec):
  if str == '':
    return 1 if rec == () else 0
  
  if rec == ():
    return 0 if '#' in str else 1

  arrangement = 0

  if str[0] in '.?':
    arrangement += count(str[1:], rec)

  if str[0] in '#?':
    if rec[0] <= len(str) and '.' not in str[:rec[0]] and (len(str) == rec[0] or str[rec[0]] != '#'):
      arrangement += count(str[rec[0] + 1:], rec[1:])

  return arrangement

for line in lines:
  pattern, record = line.split()
  pattern = '?'.join([pattern] * 5)
  record = tuple(map(int, ','.join([record] * 5).split(',')))

  res += count(pattern, record)

print(res)