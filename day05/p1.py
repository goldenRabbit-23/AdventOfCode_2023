import sys

data = open(sys.argv[1]).read().split('\n\n')
seeds = list(map(int, data[0].split(': ')[1].split()))
seedToSoil = [[int(num) for num in item.split()]
              for item in data[1].split(':\n')[1].split('\n')]
soilToFertilizer = [[int(num) for num in item.split()]
                    for item in data[2].split(':\n')[1].split('\n')]
fertilizerToWater = [[int(num) for num in item.split()]
                     for item in data[3].split(':\n')[1].split('\n')]
waterToLight = [[int(num) for num in item.split()]
                for item in data[4].split(':\n')[1].split('\n')]
lightToTemperature = [[int(num) for num in item.split()]
                      for item in data[5].split(':\n')[1].split('\n')]
temperatureToHumidity = [[int(num) for num in item.split()]
                         for item in data[6].split(':\n')[1].split('\n')]
humidityToLocation = [[int(num) for num in item.split()]
                      for item in data[7].split(':\n')[1].split('\n')]
soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []

for seed in seeds:
  found = False
  for e in seedToSoil:
    if e[1] <= seed < e[1] + e[2]:
      found = True
      soils.append(seed - e[1] + e[0])
      break
  if not found:
    soils.append(seed)

for soil in soils:
  found = False
  for e in soilToFertilizer:
    if e[1] <= soil < e[1] + e[2]:
      found = True
      fertilizers.append(soil - e[1] + e[0])
      break
  if not found:
    fertilizers.append(soil)

for fertilizer in fertilizers:
  found = False
  for e in fertilizerToWater:
    if e[1] <= fertilizer < e[1] + e[2]:
      found = True
      waters.append(fertilizer - e[1] + e[0])
      break
  if not found:
    waters.append(fertilizer)

for water in waters:
  found = False
  for e in waterToLight:
    if e[1] <= water < e[1] + e[2]:
      found = True
      lights.append(water - e[1] + e[0])
      break
  if not found:
    lights.append(water)

for light in lights:
  found = False
  for e in lightToTemperature:
    if e[1] <= light < e[1] + e[2]:
      found = True
      temperatures.append(light - e[1] + e[0])
      break
  if not found:
    temperatures.append(light)

for temperature in temperatures:
  found = False
  for e in temperatureToHumidity:
    if e[1] <= temperature < e[1] + e[2]:
      found = True
      humidities.append(temperature - e[1] + e[0])
      break
  if not found:
    humidities.append(temperature)

for humidity in humidities:
  found = False
  for e in humidityToLocation:
    if e[1] <= humidity < e[1] + e[2]:
      found = True
      locations.append(humidity - e[1] + e[0])
      break
  if not found:
    locations.append(humidity)

print(min(locations))
