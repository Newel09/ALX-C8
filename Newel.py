fruits = ["apple", "banana", "cherry", "date"]

for f in fruits:
    if f == "banana":
        continue   # skip printing banana
    if f == "date":
        break      # stop the loop when we reach date
    print(f)