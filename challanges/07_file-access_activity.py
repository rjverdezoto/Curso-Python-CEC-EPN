file = open("devices.txt","a")
while True:
    newItem = input("Enter a new item (or exit): ")
    if newItem == "exit":
        break
    else:
        file.write(newItem+"\n")
file.close()
print("All done!")
