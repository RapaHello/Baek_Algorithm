N = int(input())
room = 1
honey = 1

while N > honey:
  honey += 6 * room
  room += 1

print(room)