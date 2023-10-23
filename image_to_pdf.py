from PIL import Image, ImageOps
import os

OUTPUT_FILENAME = 'Stamp Paper.pdf'

if __name__ == '__main__':
    folder_path = "C:\\Users\\Documents\"
    # no_of_files = list(range(1, 19))
    images = ["Stamp Paper 1.jpeg", "Stamp Paper 2.jpeg"]
    pil_images = []

    try:
        # for count in no_of_files:
        #     image = os.path.join(folder_path, "Page {}.jpg".format(str(count)))
        for name in images:
            image = os.path.join(folder_path, name)
            pil_images.append(ImageOps.exif_transpose(Image.open(image)))

        convert_pil_images = []

        for pil_image in pil_images:
            convert_pil_images.append(pil_image.convert('RGB'))

        image_list = convert_pil_images[1:]

        convert_pil_images[0].save(os.path.join(folder_path, OUTPUT_FILENAME), save_all = True, append_images = image_list)

    except Exception as e:
        print('Error: {0}\nException message: {1}'.format(type(e).__name__, e))