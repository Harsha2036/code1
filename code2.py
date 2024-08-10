from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_value = pixels[x, y]
            encrypted_pixel_value = (pixel_value[0] ^ key, pixel_value[1] ^ key, pixel_value[2] ^ key)
            pixels[x, y] = encrypted_pixel_value
    image.save("encrypted_image.png")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_value = pixels[x, y]
            decrypted_pixel_value = (pixel_value[0] ^ key, pixel_value[1] ^ key, pixel_value[2] ^ key)
            pixels[x, y] = decrypted_pixel_value
    image.save("decrypted_image.png")

def main():
    image_path = input("Enter the path of the image: ")
    key = int(input("Enter the key for encryption and decryption: "))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt the image? ")
    if choice.upper() == "E":
        encrypt_image(image_path, key)
        print("Encryption done. Encrypted image saved as encrypted_image.png")
    elif choice.upper() == "D":
        decrypt_image(image_path, key)
        print("Decryption done. Decrypted image saved as decrypted_image.png")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
