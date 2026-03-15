file = open("temp.txt","r")
sstr = input("Enter word to search for: ")

file_data = file.read()
char_count = len(file_data)
word_count = len(file_data.split())
sstr_count = file_data.split().count(sstr)
line_count = len(file_data.split('\n'))

print("Character count: ",char_count)
print("Word count: ",word_count)
print("Line count: ",line_count)
print("Occurences of given word: ",sstr_count)

file.close()
