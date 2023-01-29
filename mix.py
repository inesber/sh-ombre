from image import Artwork
from PIL import Image

art1 = Artwork()
art2 = Artwork()

new_art = Image.blend(art1.img, art2.img, 0.5)
new_art.save("mix.png")
