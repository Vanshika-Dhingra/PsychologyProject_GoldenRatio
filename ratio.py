from PIL import Image

def calculate_black_to_white_ratio(image_path):
    try:
        # Load the image
        image = Image.open(image_path)

        # Convert the image to RGBA mode to include alpha (transparency) channel
        image = image.convert("RGBA")

        # Get pixel data
        pixels = list(image.getdata())

        # Count black (0) and white (255) pixels while excluding transparent pixels
        black_pixels = 0
        white_pixels = 0

        for pixel in pixels:
            r, g, b, a = pixel
            if a > 0:  # Exclude transparent pixels
                if r == 0 and g == 0 and b == 0:
                    black_pixels += 1
                elif r == 255 and g == 255 and b == 255:
                    white_pixels += 1

        # Calculate the ratio
        if white_pixels == 0:
            ratio = 0  # To avoid division by zero
        else:
            ratio = max(black_pixels / white_pixels, white_pixels / black_pixels)

        return black_pixels, white_pixels, ratio

    except Exception as e:
        return None

# Specify the path to your image
image_path = "./experiment2_shapes/1xShapes/square.png"

result = calculate_black_to_white_ratio(image_path)

if result:
    black_pixels, white_pixels, ratio = result
    print(f"Black Pixels: {black_pixels}")
    print(f"White Pixels: {white_pixels}")
    print(f"Black to White Ratio: {ratio:.2f}")
else:
    print("Error loading the image or calculating the ratio.")