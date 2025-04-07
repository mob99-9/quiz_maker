# make a text file with questions and possible answers from the user

# make a text file 

file_name = "quiz.txt"

# adds title on the quiz file

with open(file_name, "w") as file:
    file.write("Quiz Maker")

# make a function for asking questions and answers
text = open("quiz.txt", "r")

print(text.read())

text.close()

# save the text file 