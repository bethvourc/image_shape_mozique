# TODO: Update code to make the image 
# conversion to mozique produce a more 
# accurate mozique image of the inputed 
# image.
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def mosaicify(image_path, shapes, output_path):
    # Load the input image
    original_image = Image.open(image_path)
    
    # Define the size of each shape
    shape_size = 20
    
    # Initialize the output image
    output_image = Image.new("RGB", original_image.size)
    
    # Create an ImageDraw object to draw shapes on the output image
    draw = ImageDraw.Draw(output_image)
    
    # Loop through the image and draw shapes based on the provided instructions
    for y in range(0, original_image.height, shape_size):
        for x in range(0, original_image.width, shape_size):
            # Get the color of the current pixel
            pixel_color = original_image.getpixel((x, y))
            
            # Choose a random shape from the list
            shape = np.random.choice(shapes)
            
            # Draw the selected shape with the pixel color
            if shape == "rectangle":
                draw.rectangle([x, y, x+shape_size, y+shape_size], fill=pixel_color)
            elif shape == "ellipse":
                draw.ellipse([x, y, x+shape_size, y+shape_size], fill=pixel_color)
            elif shape == "polygon":
                draw.regular_polygon([x, y, x+shape_size, y+shape_size], fill=pixel_color, n_sides=5) # TODO: add number of sides 
            # Add more shape options here
            
    # Save the final mosaic image
    output_image.save(output_path)
    
    # Display the mosaic using matplotlib
    plt.imshow(output_image)
    plt.axis('off')
    plt.show()

# TODO: add input image file directory
input_image_path = "/mnt/chromeos/MyFiles/Downloads/goat.jpg"
output_image_path = "/mnt/chromeos/MyFiles/Downloads/output_mosaic.jpg"
user_shapes = ["rectangle", "ellipse","polygon"]

mosaicify(input_image_path, user_shapes, output_image_path)
