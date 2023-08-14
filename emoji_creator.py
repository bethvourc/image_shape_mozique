from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def mosaicify(image_path, emojis, output_path):
    original_image = Image.open(image_path)
    emoji_size = 20  # Adjust the size to fit your preference
    output_image = Image.new("RGB", original_image.size)
    
    emoji_map = {}  # Dictionary to map pixel colors to emojis
    for color, emoji in emojis.items():
        emoji_map[color] = emoji
    
    for y in range(0, original_image.height, emoji_size):
        for x in range(0, original_image.width, emoji_size):
            pixel_color = original_image.getpixel((x, y))
            
            if pixel_color in emoji_map:
                emoji = emoji_map[pixel_color]
                emoji_image = Image.new("RGB", (emoji_size, emoji_size), pixel_color)
                output_image.paste(emoji_image, (x, y))
    
    output_image.save(output_path)
    
    plt.imshow(output_image)
    plt.axis('off')
    plt.show()

input_image_path = "/mnt/chromeos/MyFiles/Downloads/goat.jpg"
output_image_path = "/mnt/chromeos/MyFiles/Downloads/output_mosaic_emojis.jpg"
user_emojis = {
    (255, 255, 255): "😀",
    (0, 0, 0): "🖤",
    (255, 0, 0): "🔴",
    (0, 255, 0): "🟢",
    (0, 0, 255): "🔵"
    # Add more color-to-emoji mappings as needed
}

mosaicify(input_image_path, user_emojis, output_image_path)

