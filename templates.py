import sys
try:
    while True:
        line=sys.stdin.readline().strip()
        if not line:
            break
        print(line)
except:
    pass