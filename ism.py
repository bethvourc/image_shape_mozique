from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def mosaicify(image_path, shapes, output_path):
    original_image = Image.open(image_path)
    shape_size = 20
    output_image = Image.new("RGB", original_image.size)
    draw = ImageDraw.Draw(output_image)
    
    for y in range(0, original_image.height, shape_size):
        for x in range(0, original_image.width, shape_size):
            pixel_color = original_image.getpixel((x, y))
            shape = np.random.choice(shapes)
            
            if shape == "rectangle":
                draw.rectangle([x, y, x+shape_size, y+shape_size], fill=pixel_color)
            elif shape == "ellipse":
                draw.ellipse([x, y, x+shape_size, y+shape_size], fill=pixel_color)
            elif shape == "polygon":
                # Calculate the center of the polygon
                center = (x + shape_size // 2, y + shape_size // 2)
                radius = shape_size // 2
                
                # Draw the regular polygon using 5 sides
                draw.regular_polygon((center, radius), n_sides=5, fill=pixel_color)
            
    output_image.save(output_path)
    
    plt.imshow(output_image)
    plt.axis('off')
    plt.show()

input_image_path = "/mnt/chromeos/MyFiles/Downloads/goat.jpg"
output_image_path = "/mnt/chromeos/MyFiles/Downloads/output_mosaic.jpg"
user_shapes = ["rectangle", "ellipse", "polygon"]

mosaicify(input_image_path, user_shapes, output_image_path)

