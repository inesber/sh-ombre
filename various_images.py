from image import Artwork
from rectangles import RectanglesArtwork
from circles import CirclesArtwork
from lines import LinesArtwork
import os

print("images")

os.makedirs("images", exist_ok=True)

for i in range(1, 5):
    filepath = os.path.join("images", f"gradient-{i}.png")

    art = Artwork(grain=i * 0.1)
    art.save_to_file(filepath)

for i in range(1, 5):
    filepath = os.path.join("images", f"rect-{i}.png")

    art = RectanglesArtwork(grain=i * 0.1)
    art.save_to_file(filepath)

for i in range(1, 5):
    filepath = os.path.join("images", f"circle-{i}.png")

    art = CirclesArtwork(debug=True)
    art.save_to_file(filepath)

for i in range(1, 5):
    filepath = os.path.join("images", f"line-{i}.png")

    art = LinesArtwork()
    art.save_to_file(filepath)
