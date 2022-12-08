#  This is not My code and Doesn't falles under my License and can be used how ever you want.
#  It is generated using GitCopilot and ChatGpt3 Correction and some modifiaction by me 
#  to make it useable for my code for basic compression. 
#  I am not going to be responsible for anyone using these code aside for this project.
#  I have right for the use for these project under GNU license and so do you.

 
import os
from PIL import Image, ImageFilter


counter = 0
def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def printf(*args):
    print(*args) if (__name__=="__main__") else '' 
    


def compress_img(
    image_name,bw=False,new_size_ratio=0.9, quality=100, width=None, height=None, to_jpg=True
):
    global counter
    print("#",counter)
    counter+=1
    img = Image.open(image_name)
    printf("[*] Image shape:", img.size)
    image_size = os.path.getsize(image_name)
    printf("[*] Size before compression:", get_size_format(image_size))
    if bw:
        img = img.filter(ImageFilter.SMOOTH_MORE) if counter==1 else img
        img = img.convert("L") if counter==1 else img
    if new_size_ratio < 1.0:

        img = img.resize(
            (int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)),
            Image.Resampling.LANCZOS,
        )
        printf("[+] New Image shape:", img.size)
    elif width and height:
        img = img.resize((width, height), Image.LANCZOS)
        printf("[+] New Image shape:", img.size)
    filename, ext = os.path.splitext(image_name)
    if to_jpg:
        new_filename = f"new_compressed.jpg"
    else:
        new_filename = f"new_compressed{ext}"
    try:
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=True)
            
    printf("[+] New file saved:", new_filename)
    new_image_size = os.path.getsize(new_filename)
    printf("[+] Size after compression:", get_size_format(new_image_size))
    saving_diff = new_image_size - image_size
    printf(
        f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size."
    )

    if __name__!="__main__":
        if (new_image_size>1024**2):
            new_size_ratio-=0.1
            compress_img(new_filename, new_size_ratio)   
    return new_filename


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Simple Python script for compressing and resizing images"
    )
    parser.add_argument("image", help="Target image to compress and/or resize")
    parser.add_argument(
        "-j",
        "--to-jpg",
        action="store_true",
        help="Whether to convert the image to the JPEG format",
    )
    parser.add_argument(
        "-q",
        "--quality",
        type=int,
        help="Quality ranging from a minimum of 0 (worst) to a maximum of 95 (best). Default is 90",
        default=90,
    )
    parser.add_argument(
        "-r",
        "--resize-ratio",
        type=float,
        help="Resizing ratio from 0 to 1, setting to 0.5 will multiply width & height of the image by 0.5. Default is 1.0",
        default=1.0,
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        help="The new width image, make sure to set it with the `height` parameter",
    )
    parser.add_argument(
        "-hh",
        "--height",
        type=int,
        help="The new height for the image, make sure to set it with the `width` parameter",
    )
    args = parser.parse_args()

    print("=" * 50)
    print("[*] Image:", args.image)
    print("[*] To JPEG:", args.to_jpg)
    print("[*] Quality:", args.quality)
    print("[*] Resizing ratio:", args.resize_ratio)
    if args.width and args.height:
        print("[*] Width:", args.width)
        print("[*] Height:", args.height)
    print("=" * 50)

    compress_img(
        args.image,
        args.resize_ratio,
        args.quality,
        args.width,
        args.height,
        args.to_jpg,
    )
