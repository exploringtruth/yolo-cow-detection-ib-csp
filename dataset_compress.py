import os
from PIL import Image

def optimize_images(root_dir, max_width=800):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                path = os.path.join(root, file)
                try:
                    with Image.open(path) as img:
                        if img.width > max_width:
                            w_percent = max_width / float(img.width)
                            h_size = int(float(img.height) * float(w_percent))
                            img = img.resize((max_width, h_size), Image.Resampling.LANCZOS)
                            img.save(path, optimize=True, quality=82)
                            print(f"Optimized: {path}")
                except Exception as e:
                    print(f"Error {path}: {e}")

optimize_images("Dataset")
optimize_images("result")
