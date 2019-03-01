from PIL import Image
import random
from pathlib import Path


class Glitcher:
	startColumn = 200
	glitchHeight = 100
	shift = 120  # positive is to the right
	mixRatio = 0.8  # ratio between original and random color in case of glitch, 0 <= mixRatio <= 1
	redBase = 255  # minimum red value in case of glitch
	greenBase = 0  # minimum green value in case of glitch
	blueBase = 0  # minimum blue value in case of glitch

	def glitch(self, filepath):
		path = Path(filepath)
		img = Image.open(filepath)
		pixels = img.load()
		pixelsCopy = img.copy().load()

		for j in range(self.startColumn, self.startColumn + self.glitchHeight):
			# Determine whether or not to glitch that column
			shouldGlitch = random.choice([True, False])

			for i in range(img.size[0]):
				# Move shift pixels to the right
				currentX = i + self.shift
				if currentX >= img.size[0]:
					currentX = currentX - img.size[0]
				# Get current colors
				red = pixelsCopy[i, j][0]
				green = pixelsCopy[i, j][1]
				blue = pixelsCopy[i, j][2]

				if shouldGlitch:
					redModifier = random.randint(self.redBase, 255)
					greenModifier = random.randint(self.greenBase, 255)
					blueModifier = random.randint(self.blueBase, 255)
					red = int(((red * (1 - self.mixRatio)) + redModifier * self.mixRatio))
					green = int(((green * (1 - self.mixRatio)) + greenModifier * self.mixRatio))
					blue = int(((blue * (1 - self.mixRatio)) + blueModifier * self.mixRatio))
				pixels[currentX, j] = (red, green, blue)

		savePath = path.parent / "edit.jpg"
		print(savePath)
		img.save(savePath)