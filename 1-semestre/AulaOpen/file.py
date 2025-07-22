with open("AulaOpen/text2.txt", "r") as f:
    for i in f:
        if "coca" in i.lower():
            print(i)