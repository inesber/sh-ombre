from PIL import Image
import os
import random
import colorsys


class Artwork:
    def __init__(self, size=(500, 500), grain=(0.1)):
        self.img = Image.new("RGBA", size)
        self.colorway = (
            self.random_color(),
            self.random_color(),
            self.random_color(),
            self.random_color()
        )
        self.grain = grain
        self.create()

    def create(self):
        for x in range(self.img.width):
            for y in range(self.img.height):
                color = self.get_color(x, y)

                self.img.putpixel((x, y), color)

    def get_color(self, x, y):
        (tl, tr, bl, br) = self.colorway

        percent_x = x / self.img.width
        percent_y = y / self.img.height

        grain_x = random.uniform(-1 * self.grain, self.grain)
        grain_y = random.uniform(-1 * self.grain, self.grain)

        gradient1 = self.mix(tl, tr, percent_x + grain_x)
        gradient2 = self.mix(bl, br, percent_x + grain_x)

        gradient = self.mix(gradient1, gradient2, percent_y + grain_y)

        return gradient

    def mix(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2

        return (
            self.mix_colors(r1, r2, mixer),
            self.mix_colors(g1, g2, mixer),
            self.mix_colors(b1, b2, mixer),
            self.mix_colors(a1, a2, mixer)
        )

    def mix_colors(self, c1, c2, mixer):
        return int(c1 + (c2 - c1) * mixer)

    def random_color(self):
        h = random.uniform(0, 1)
        s = random.uniform(0.5, 0.8)
        v = random.uniform(0.8, 1)

        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        return (r, g, b, 255)

    def save_to_file(self, filepath):
        self.img.save(filepath)


if __name__ == "__main__":
    print("images")
    os.makedirs("images", exist_ok=True)
    filepath = os.path.join("images", "test.png")

    art = Artwork()
    art.save_to_file(filepath)
