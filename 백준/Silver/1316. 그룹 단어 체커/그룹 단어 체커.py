N = int(input())
group = []

for i in range(N):
  word = input()
  diff = 0

  for j in range(len(word) - 1):
    if word[j] != word[j + 1]: 
      word2 = word[j + 1 :]
      if word2.count(word[j]) > 0: diff = 1

  if diff == 0: group.append(word)

print(len(group))