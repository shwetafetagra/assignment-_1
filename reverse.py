letter = input("Enter a word to reverse: ")
for char in range(len(letter)-1, -1, -1 ):
  print(letter[char], end="")