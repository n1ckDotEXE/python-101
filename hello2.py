prompt_text = 'What is your name? '
name = input(prompt_text.upper())

greeting = f'Hello, {name}!'
print(greeting.upper())

about_name = f'Your name has {len(name)} letters in it! Awesome!'
print(about_name)