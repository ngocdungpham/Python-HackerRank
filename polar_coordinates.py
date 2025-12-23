import cmath

z = complex(input())

print(abs(z))
print(cmath.phase(z))
print(cmath.phase(z))       # Argument (phase angle)
print(abs(z))               # Magnitude (modulus)
print(cmath.polar(z))       # (magnitude, phase)
print(cmath.rect(2, cmath.pi/4))  # Convert polar to rectangular