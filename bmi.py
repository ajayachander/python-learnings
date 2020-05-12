def bmi(weight, height):
    if weight < 0 or weight > 150:
        return None
    if height < 0.5 or height > 2.25:
        return None 
    return weight / height ** 2

print(bmi(52.5, 1.65))
print(bmi(165,2.0))
print(bmi(100, 2.4))
print(bmi(75,1.65))
