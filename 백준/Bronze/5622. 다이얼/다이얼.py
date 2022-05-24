dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dial2 = input()
sum = 0

for i in range(len(dial2)):
  for j in dial:
    if dial2[i] in j:
      sum += dial.index(j) + 3

print(sum)