import random

WIDTH, HEIGHT = 30, 9
STAR_COUNT = 42
STARS = ("·", "·", "✧", "✦")


def draw_sky(rng):
	 sky = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
	 positions = rng.sample(range(WIDTH * HEIGHT), STAR_COUNT)
	 for position in positions:
		y, x = divmod(position, WIDTH)
		sky[y][x] = rng.choice(STARS)
	 return sky


def print_frame(rows):
	print("╭" + "─" * WIDTH + "╮")
	for row in rows:
		print("│" + "".join(row) + "│")
	print("╰" + "─" * WIDTH + "╯")


def main():
	rng = random.SystemRandom()
	print_frame(draw_sky(rng))

	poem = rng.choice((
		("The moon hums softly", "Silver comets cross the night", "And dawn finds us here"),
		("A small star listens", "Night folds its blue wings around us", "The dark blooms with light"),
		("Worlds drift, quiet as", "Old wishes sailing through the dark", "Somewhere, you begin"),
	))
	print("\n" + "\n".join(poem))
	print("\nYour coordinates: somewhere wonderful.")


if __name__ == "__main__":
	main()
