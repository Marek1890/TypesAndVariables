###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area - pole
# calculate circumference - obwód
# print results

radius = input('Enter circle radius: ')
radius = float(radius)
pi = 3.14
circumference = round(2 * pi * radius, 2)
area = round(pi * radius * radius, 2)
print(f'Circle circumference: {circumference}')
print(f'Circle area: {area}')