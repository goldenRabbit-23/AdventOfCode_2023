import sys
import re

lines = open(sys.argv[1]).read().splitlines()
pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
res = 0

word_dict = {
  'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

for line in lines:
  matches = re.findall(pattern, line)
  digits = [int(word_dict.get(item, item)) for item in matches]
  res += digits[0] * 10 + digits[-1]

print(res)