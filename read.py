try:
    f = open("info1.txt", "r")
    lines = f.readline()
    print(lines)
except Exception:
    print(Exception)