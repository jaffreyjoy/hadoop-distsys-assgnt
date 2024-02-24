
fs = ""
with open("input.txt") as f:
    fs = f.read().strip()
with open("input.txt", "w") as f:
    f.write(fs.replace(":","\t"))