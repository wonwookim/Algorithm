import sys

a = int(sys.stdin.readline())
count = 1
room = 1

while room < a:
    room += (6 * count)
    count += 1

print(count)