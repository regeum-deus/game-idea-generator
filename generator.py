from random import randint

genres = []
with open("./genres.data") as f:
	genres = f.readlines()
themes = []
with open("./themes.data") as f:
	themes = f.readlines()

print("-########GAME IDEA GENERATOR########-")

while True:
	print("genre: " + genres[randint(0, len(genres) - 1)] + "\ntheme: " + themes[randint(0, len(themes) - 1)] + "\n")
	input()
