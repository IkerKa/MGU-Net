import os
from PIL import Image
import numpy as np

mask_dir = 'data/dataset/val/mask'
all_vals = set()
for fname in os.listdir(mask_dir):
    mask = Image.open(os.path.join(mask_dir, fname))
    vals = np.unique(np.array(mask))
    all_vals.update(vals)
print("Valores únicos en todas las máscaras:", sorted(all_vals))