from PIL import Image
from noise import pnoise2
import os
import random
import colorsys


class Artwork:
    def __init__(self, size=(500, 500), grain=(0), noise_density=2.5, noise_shift=2.0):
        self.img = Image.new("RGBA", size)
        self.colorway = (
            self.random_color(),
            self.random_color(),
            self.random_color(),
            self.random_color()
        )
        self.noise_density = noise_density
        self.noise_shift = noise_shift
        self.noise_base = random.randint(0, 999)
        self.grain = grain
        self.create()

    def get_random_points(self):
        points = []
        for x in range(self.img.width):
            for y in range(self.img.height):
                points.append((x, y))

        random.shuffle(points)

        return points

    def create(self):
        for (x, y) in self.get_random_points():
            color = self.get_color(x, y)
            self.img.putpixel((x, y), color)

    def make_grain(self):
        if self.grain > 0:
            return random.uniform(
                -1 * self.grain,
                self.grain)
        else:
            return 0

    def make_noise(self, percent_x, percernt_y):

        return self.noise_density * pnoise2(
            percent_x * self.noise_shift,
            percernt_y * self.noise_shift,
            base=self.noise_base)

    def get_color(self, x, y):
        (tl, tr, bl, br) = self.colorway

        percent_x = x / self.img.width
        percent_y = y / self.img.height

        grain_x = self.make_grain()
        grain_y = self.make_grain()

        noise_x = self.make_noise(percent_x, percent_y)
        noise_y = self.make_noise(percent_x, percent_y)

        gradient1 = self.mix(tl, tr, percent_x + grain_x + noise_x)
        gradient2 = self.mix(bl, br, percent_x + grain_x + noise_x)

        gradient = self.mix(gradient1, gradient2,
                            percent_y + grain_y + noise_y)

        return gradient

    def mix(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2

        mixer = max(0, min(mixer, 1))

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
