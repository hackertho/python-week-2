name=input("enter your name: ")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[1]}: {name.count(name[i])}")
        temp+=name[1]