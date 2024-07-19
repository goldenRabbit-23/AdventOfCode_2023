import sys

lines = open(sys.argv[1]).readlines()
ans = 0

for line in lines:
  line = line.strip()
  body = line.split(': ')[1]
  sets = body.split('; ')

  max_red = max_green = max_blue = 0
  for set in sets:
    cubes = set.split(', ')
    red = green = blue = 0

    for cube in cubes:
      count, color = cube.split(' ')
      if color == 'red':
        red = int(count)
      if color == 'green':
        green = int(count)
      if color == 'blue':
        blue = int(count)

    max_red = max(max_red, red)
    max_green = max(max_green, green)
    max_blue = max(max_blue, blue)

  ans += max_red * max_green * max_blue

print(ans)
