devices=["R1","R2","R3","S1","S2"]

print("All Items in devices")
for item in devices:
    print(item)

print()
print("Items with R")

for item in devices:
    if "R" in item:
        print(item)

switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)

