from image import Artwork
from PIL import ImageDraw
import os
import random
import math


class LinesArtwork(Artwork):
    def create(self):
        drawer = ImageDraw.Draw(self.img)

        for (x, y) in self.get_random_points():
            color = self.get_color(x, y)

            length = random.randint(3, 15)
            angle = random.uniform(0, 3.141)

            sx = length * math.sin(angle)
            sy = length * math.cos(angle)

            drawer.line([
                (x - sx, y - sy),
                (x + sx, y + sy)
            ], fill=color)


if __name__ == "__main__":
    print("lines")
    os.makedirs("images", exist_ok=True)
    filepath = os.path.join("images", "lines.png")

    art = LinesArtwork()
    art.save_to_file(filepath)
