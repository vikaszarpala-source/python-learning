text = input("Enter a string: ")

for char in set(text):
    print(char, "=", text.count(char))


    text = input("Enter a string: ")

characters = set(text)
most_repeated = max(characters, key=text.count)

print("Most repeated character:", most_repeated)
print("Count:", text.count(most_repeated))