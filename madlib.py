# Prompt the user for the missing words to a Madlib sentence using the input function.
name = ''
subject = '' 
result = ''

prompt_text = 'Please fill in the blanks below:'
example_madlib = "___(name)___'s favorite subject in school is ___(subject)___."

print(prompt_text)
print(example_madlib)

name = input('What is your name? ')
subject = input('What is your favorite subject? ')

result = f"{name}'s favorite subject in school is {subject}."


# Print the madlib
print(result)
