from image import Artwork
import os

print("images")

os.makedirs("export", exist_ok=True)

filepath = os.path.join("export", "export.png")

art = Artwork((2000, 2000))
art.save_to_file(filepath)
