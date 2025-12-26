import math

ab=int(input())
bc=int(input())

mc= math.sqrt(ab**2 + bc**2)/2
tan_c = ab/bc
goc_radians = math.atan(tan_c)
degrees_c = math.degrees(goc_radians)
print(f"{round(degrees_c)}\u00B0")
