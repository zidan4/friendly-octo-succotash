import random


def main():
	rng = random.SystemRandom()
	width, height = 30, 9
	sky = [[" " for _ in range(width)] for _ in range(height)]

	for _ in range(42):
		x, y = rng.randrange(width), rng.randrange(height)
		sky[y][x] = rng.choice(("·", "·", "✧", "✦"))

	print("╭" + "─" * width + "╮")
	for row in sky:
		print("│" + "".join(row) + "│")
	print("╰" + "─" * width + "╯")

	poem = rng.choice((
		("The moon hums softly", "Silver comets cross the night", "And dawn finds us here"),
		("A small star listens", "Night folds its blue wings around us", "The dark blooms with light"),
		("Worlds drift, quiet as", "Old wishes sailing through the dark", "Somewhere, you begin"),
	))
	print("\n" + "\n".join(poem))
	print("\nYour coordinates: somewhere wonderful.")


if __name__ == "__main__":
	main()
