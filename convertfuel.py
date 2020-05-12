def l100kmtompg(liters):
    metreperml = (100 / liters)
    mileperml = metreperml/1609.344
    milepergal = mileperml*3785.411784 
    return milepergal

def mpgtol100km(miles):
    mileperml =  miles / 3785.411784
    metreperml = mileperml * 1609.344
    lper100km = 100/metreperml
    return lper100km
    

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))