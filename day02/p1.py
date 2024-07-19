import sys

lines = open(sys.argv[1]).readlines()
ans = 0
game = 1

for line in lines:
  flag = True

  line = line.strip()
  body = line.split(': ')[1]
  sets = body.split('; ')

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

    if red > 12 or green > 13 or blue > 14:
      flag = False
      break

  if flag:
    ans += game

  game += 1

print(ans)
