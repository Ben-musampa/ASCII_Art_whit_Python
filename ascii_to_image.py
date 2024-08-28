from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Caractères ASCII du plus sombre au plus clair
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
    return ascii_img

def draw_ascii_on_image(ascii_art, new_width=100, font_size=100):
    """Dessine l'ASCII Art sur une nouvelle image."""
    # Calculer la taille de l'image en fonction de la longueur du texte et de la taille de la police
    font = ImageFont.load_default()
    char_width = font.getsize("A")[0]
    char_height = font.getsize("A")[1]
    image_width = new_width * char_width
    image_height = len(ascii_art.splitlines()) * char_height

    # Créer une nouvelle image blanche
    new_image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(new_image)

    # Dessiner chaque ligne d'ASCII sur l'image
    y_offset = 0
    for line in ascii_art.splitlines():
        draw.text((0, y_offset), line, fill="black", font=font)
        y_offset += char_height

    # Sauvegarder ou afficher l'image
    new_image.save("ascii_art_image.png")
    new_image.show()

# Utilisation
image_path = "IMG_6128.JPG"  # Remplace par le chemin de ton image
ascii_art = image_to_ascii(image_path)
draw_ascii_on_image(ascii_art)
