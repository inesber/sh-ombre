from image import Artwork
from PIL import ImageDraw
import os
import random


class CirclesArtwork(Artwork):
    def create(self):
        drawer = ImageDraw.Draw(self.img)

        for (x, y) in self.get_random_points():
            color = self.get_color(x, y)

            radius = random.randint(3, 15)

            drawer.ellipse([
                (x - radius, y - radius),
                (x + radius, y + radius)
            ], fill=color)


if __name__ == "__main__":
    print("circles")
    os.makedirs("images", exist_ok=True)
    filepath = os.path.join("images", "circles.png")

    art = CirclesArtwork()
    art.save_to_file(filepath)
