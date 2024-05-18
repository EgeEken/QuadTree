import numpy as np
from PIL import Image
import os

original = "original.png"
file1 = "file1.png"
file2 = "file2.png"

img1 = np.array(Image.open(original))
img2 = np.array(Image.open(file1))
img3 = np.array(Image.open(file2))

loss_mean = (np.abs(img1.astype(np.int16) - img2).astype(np.uint8))
loss_max = (np.abs(img1.astype(np.int16) - img3).astype(np.uint8))

original_size = round(os.path.getsize(original)/1000, 2)
file1_size = round(os.path.getsize(file1)/1000, 2)
file2_size = round(os.path.getsize(file2)/1000, 2)

print("\n")
print(f"MEAN: {round(np.mean(loss_mean > 10) * 100, 2)}% information loss, {round(100 * (1 - file1_size/original_size), 2)}% size reduction")
print(f"MAX: {round(np.mean(loss_max > 10) * 100, 2)}% information loss, {round(100 * (1 - file2_size/original_size), 2)}% size reduction")
print("\n")