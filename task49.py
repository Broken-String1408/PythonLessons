import math

def squer_orbits(r1, r2):
    return math.pi * r1 * r2

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

filtered_orbits = list(filter(lambda x: x[0] != x[1], orbits))
max_orbit = max(list(map(lambda a: squer_orbits(a[0], a[1]), filtered_orbits)))
result = list(filter(lambda a: max_orbit == squer_orbits(a[0], a[1]), orbits))

print(filtered_orbits)
print(max_orbit)

print(*result[0])