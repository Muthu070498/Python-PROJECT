colors={'nepal','Yellow','Orange'}
country={'India','Blue','China','nepal','America','India'}

print(country)
print(colors)

# country.add('Japan')
# print(country)
#
# country.pop()
# print(country)
#
# country.remove('chennai')
# print(country)

# country.discard('chennai')
# print(country)
#
# country.update(colors)
# print(country)

# country.union()
# country.difference_update(colors)
# print(country)

country.symmetric_difference_update(colors)
print(country)