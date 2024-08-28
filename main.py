from PIL import Image
import numpy as np

# Caractères ASCII en fonction de la luminosité (du plus sombre au plus clair)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Redimensionne l'image en conservant le ratio d'aspect."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Convertit l'image en niveaux de gris."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Mappe chaque pixel à un caractère ASCII."""
    pixels = np.array(image)
    ascii_str = ""
    for pixel in pixels.flatten():
        ascii_str += ASCII_CHARS[pixel // 32]  # Divise par 32 pour correspondre à la plage des caractères ASCII
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Convertit l'image en ASCII."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Impossible d'ouvrir le fichier image {image_path}. {e}")
        return

    image = resize_image(image, new_width)
    grayscale = grayscale_image(image)
    ascii_str = pixels_to_ascii(grayscale)

    # Diviser la chaîne ASCII en lignes de largeur 'new_width'
    ascii_img = "\n".join([ascii_str[i:(i+new_width)] for i in range(0, len(ascii_str), new_width)])
    print(ascii_img)

    # Optionnel : Sauvegarder le résultat dans un fichier texte
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

# Utilisation
image_path = "IMG_6128.JPG"  # Remplace par le chemin de ton image
image_to_ascii(image_path)
