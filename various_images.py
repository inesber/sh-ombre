from image import Artwork
import os

print("images")

os.makedirs("images", exist_ok=True)

for i in range(1, 11):
    filepath = os.path.join("images", f"image-{i}.png")

    art = Artwork()
    art.save_to_file(filepath)
