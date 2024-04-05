from PIL import Image, ImageChops

# Load the images
image1_path = 'Selfie on the moonnowatermark.png'
image2_path = 'Selfie on the moon.png'
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Convert images to the same mode and size if necessary
if image1.mode != image2.mode or image1.size != image2.size:
    image1 = image1.convert('RGB')
    image2 = image2.convert('RGB')
    image1 = image1.resize(image2.size)

# Find differences
diff = ImageChops.difference(image1, image2)

# Check if there's any difference
bbox = diff.getbbox()
if bbox is not None:
    # Highlight differences
    diff = diff.point(lambda x: x > 0 and 255)
    mask = diff.convert("1")
    image_highlighted = image2.copy()
    image_highlighted.paste(Image.new("RGB", image2.size, "red"), mask=mask)
else:
    image_highlighted = None

# Save or show result
if image_highlighted:
    highlighted_path = 'difference_highlighted.png'
    image_highlighted.save(highlighted_path)
    result = highlighted_path
else:
    result = "No differences found."

result
