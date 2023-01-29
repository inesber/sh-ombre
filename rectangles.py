from image import Artwork
from PIL import ImageDraw
import os
import random


class RectanglesArtwork(Artwork):
    def create(self):
        drawer = ImageDraw.Draw(self.img)

        for (x, y) in self.get_random_points():
            color = self.get_color(x, y)

            width = random.randint(3, 15)
            height = random.randint(3, 15)

            drawer.rectangle([
                (x - width, y - height),
                (x + width, y + height)
            ], fill=color)


if __name__ == "__main__":
    print("rectangles")
    os.makedirs("images", exist_ok=True)
    filepath = os.path.join("images", "rectangles.png")

    art = RectanglesArtwork()
    art.save_to_file(filepath)
