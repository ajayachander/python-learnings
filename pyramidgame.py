blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 0

while blocks != 0:
    layer = layer + (blocks - (blocks - 1))
    height = height + 1
    blocks = blocks - layer
    
    if layer >= blocks: break

print("The height of the pyramid:", height)