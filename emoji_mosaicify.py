from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

def mosaicify(image_path, emojis, output_path):
    original_image = Image.open(image_path)
    shape_size = 20 
    output_image = Image.new("RGB", original_image.size)  # Remove the color specification here
    draw = ImageDraw.Draw(output_image)
    
    # Load a Unicode-compatible font for rendering emojis
    font = ImageFont.truetype("path_to_your_unicode_font.ttf", 15)  # Replace with the path to your font
    
    for y in range(0, original_image.height, shape_size):
        for x in range(0, original_image.width, shape_size):
            pixel_color = original_image.getpixel((x, y))
            emoji = emojis[np.random.randint(0, len(emojis))]
            
            draw.text((x, y), emoji, fill=pixel_color, font=font)  # Use the loaded font
            
    output_image.save(output_path)
    
    plt.imshow(output_image)
    plt.axis('off')
    plt.show()

input_image_path = "/mnt/chromeos/MyFiles/Downloads/goat.jpg"
output_image_path = "/mnt/chromeos/MyFiles/Downloads/output_mosaic_emoji.jpg"
user_emojis = ["😀", "😁", "😂", "🤣","🖤"]

mosaicify(input_image_path, user_emojis, output_image_path)