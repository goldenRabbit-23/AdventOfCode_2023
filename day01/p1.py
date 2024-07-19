import sys
import re

lines = open(sys.argv[1]).read().splitlines()
res = 0

for line in lines:
  digits = re.findall(r'\d', line)
  res += int(digits[0] + digits[-1])

print(res)