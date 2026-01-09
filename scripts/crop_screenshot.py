from PIL import Image
import sys

src = 'assets/screenshot.png'
out = 'assets/screenshot.png'

# desired crop
crop_w, crop_h, off_x, off_y = 1280, 600, 40, 80

try:
    img = Image.open(src)
except Exception as e:
    print(f'ERROR: could not open {src}:', e)
    sys.exit(1)

w,h = img.size
print('Original size:', w,h)

# check if desired box fits
if off_x+crop_w <= w and off_y+crop_h <= h:
    box = (off_x, off_y, off_x+crop_w, off_y+crop_h)
    cropped = img.crop(box)
    print('Cropped using requested box:', box)
else:
    # fallback: center crop to desired aspect ratio
    target_w = min(crop_w, w)
    target_h = min(crop_h, h)
    left = max(0, (w - target_w)//2)
    top = max(0, (h - target_h)//2)
    box = (left, top, left+target_w, top+target_h)
    cropped = img.crop(box)
    print('Fallback center crop box:', box)

# save as PNG
try:
    cropped.save(out)
    print('Saved cropped image to', out)
except Exception as e:
    print('ERROR saving image:', e)
    sys.exit(1)
