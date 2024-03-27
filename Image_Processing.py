#PIL: Python Imaging Library
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageColor

print(
    "Basics you need to remember before going deep\n"
    "1. open the image using .open(filename)\n"
    "to open the image '.show()'\n"
    "to rotate the image at any degrees '.rotate(degrees)'\n"
    "to see the mode of the image 'image.mode'\n"
    "to see the format of the image 'image.format'\n"
    "to see the size of the image 'image.size'\n"
    "to see the see the info of image 'image.info'(imformations will be in dictnoary)"
    )

#blurs the image according what the user want
def blur(image, Blur_type):        
    if Blur_type == 1:
        return image.filter(ImageFilter.BLUR)
    elif Blur_type == 2:
        n = float(input("Enter the radius: ")) 
        return image.filter(ImageFilter.BoxBlur(n))
    else:
        n = float(input("Enter the radius: ")) 
        return image.filter(ImageFilter.GaussianBlur(n))

#crops the images from the co-ordinates
def crop(image, crop_choice):
    left = int(input("Enter the left coordinate:"))
    top = int(input("Enter the top coordinate:"))
    right = int(input("Enter the right coordinate:"))
    bottom = int(input("Enter the bottom coordinate:"))
    
    box = (left,top,right,bottom)

    return image.crop(box)

#adds the watermark on the image in which user wanted to have the font style
def watermark(image, water_mark):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    type = input("Enter the font style: ")
    size = int(input("Enter the size for words:"))
    text = input("what you want to enter as water marks:")
    font = ImageFont.truetype(type, size)
    textwidth, textheight = draw.textsize(text, font)
    margin = int(input("enter the margin: "))
    coordinate_x = width - textwidth - margin
    coordinate_y = height - textheight- margin
    draw.text((coordinate_x,coordinate_y), text, font = font)
    return image

#merging of 2 picture that user wants
def mergepicture(image, second_image):
    width = int(input("Enter width:"))
    height = int(input("Enter height:"))
    image = image.resize((width, height))

    image_size = image.size
    second_image_size = second_image.size

    new_img = Image.new('RGB',(2*image_size[0], image_size[1]),(250, 250, 250))
    new_img.paste(image,(0,0))
    new_img.paste(second_image, (image_size[0],0))

    return new_img

#if user wants to create thumbnail of picture
def thumb(image, thumbnail_choice):
    b = int(input("Enter the width: "))
    h = int(input("Enter the height: "))
    try:
        image.thumbnail((b, h))
        return image
    except IOError:
        print("Error: Could not create thumbnail.")
        return None

#if user wants to flip the image
def flip_image(image, flip_type):
    if flip_type == 1:
        image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    elif flip_type == 2:
        image1 = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    elif flip_type == 3:
        image1 = image.transpose(Image.ROTATE_90)
    
    elif flip_type == 4:
        image1 = image.transpose(Image.ROTATE_180)
    
    elif flip_type == 5:
        image1 = image.transpose(Image.ROTATE_270)
    
    else:
        image1 = image.transpose(Image.BICUBIC)
    
    return image1

#if user wants to resize the image that they had using breath and height
def sizing(image, resizing):
    b = float(input("enter the width: "))
    h = float(input("enter the height: "))
    resized_img = image.resize((round(image.size[0]*b), round(image.size[1]*h)))

    return resized_img

#if user want the more filters to image
def Minifilters(image, filter_choice):
    if filter_choice == 1:
        image = image.filter(ImageFilter.BLUR)
    elif filter_choice == 2:
        image = image.filter(ImageFilter.DETAIL)
    elif filter_choice == 3:
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_choice == 4:
        image = image.filter(ImageFilter.EDGE_ENHANCE)
        more = input("if you want more edge enhanced(yes/no): ")
        if more == "yes" or more == "Yes":
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter_choice == 5:
        image = image.filter(ImageFilter.EMBOSS)
    elif filter_choice == 6:
        image = image.filter(ImageFilter.FIND_EDGES)
    elif filter_choice == 7:
        image = image.filter(ImageFilter.SHARPEN)
    elif filter_choice == 8:
        image = image.filter(ImageFilter.SMOOTH)
        more = input("if you want more smoothness(yes/no): ")
        if more == "yes" or more == "Yes":
            image = image.filter(ImageFilter.SMOOTH_MORE)
    return image

#if user want to see intesity of the colors
def getcolor():
    color_name = input("Enter the color name: ")
    color_value = ImageColor.getcolor(color_name, "RGB")
    return color_value

#if user want to seprate the colour RGB from the image
def grey_pic(image, grey_choice):
    zeroed_band = Image.new("L", image.size, 0) 
    if grey_choice == 1:
        grey_img = image.convert("L")
    
    else:
        red, green, blue = image.split()
        if grey_choice == 2:
            grey_img = Image.merge(
                "RGB",(red, zeroed_band, zeroed_band)
            )
        elif grey_choice == 3:
            grey_img = Image.merge(
                "RGB",(zeroed_band, green, zeroed_band)
            )
        elif grey_choice == 4:
            grey_img = Image.merge(
                "RGB",(zeroed_band, zeroed_band, blue)
            )
    return grey_img


# opening of image and starting point
try:
    im = input("Enter the Image file with extension: ")
    original_image = Image.open(im)
    original_image.show()
except IOError:
    print("Image didn't open successfully")

if original_image.mode != "RGB":
        original_image = original_image.convert("RGB")

Blur_choice = input("If you want to Blur Image (yes/no): ")
if Blur_choice.lower() == "yes":
    print("Which Blur do you want:\n 1. Simple\n 2. Box\n 3. Gaussian\n")
    Blur_type = int(input("Enter the type of blur: "))
    original_image = blur(original_image, Blur_type)

Crop_choice = input("if you want to crop Image(yes/no): ")
if Crop_choice.lower() == "yes":
    original_image = crop(original_image, Crop_choice)

water_mark = input("if you want to have water mark(yes/no): ")
if water_mark.lower() == "yes":
    original_image = watermark(original_image, water_mark)

merge_picture = input("if you want to have 2 pictures merged(yes/no): ")
if merge_picture.lower() == "yes":
        new_image = input("Enter the Filename with extension: ")
        second_image = Image.open(new_image)
        original_image = mergepicture(original_image, second_image)

thumbnail = input("if you want to have thumbnail of picture(yes/no): ")
if thumbnail.lower() == "yes":
    original_image = thumb(original_image, thumbnail)

flip = input("if you want to have image flipped(yes/no): ")
if flip.lower() == "yes":
    print("Which type of flip you want:\n 1. horizontal\n 2. vertical\n 3. Rotate 90\n 4. Rotate 180\n 5. Rotate 270\n 6. Bicubic ")
    Flip_type = int(input("Enter the type of flip:"))
    original_image = flip_image(original_image, Flip_type)

resizing = input("if you want image resized(yes/no): ")
if resizing.lower() == "yes":
    original_image = sizing(original_image, resizing)

filters = input("if you want more filters(yes/no): ")
if filters.lower() == "yes":
    print("Which type of filter you want:\n 1. Blur\n 2. Detail\n 3. Countour\n 4. Edge_Enhance\n 5. Emboss\n 6. Find_Edges\n 7. Sharpen\n 8. Smooth\n ")
    filter_choice = int(input())
    original_image = Minifilters(original_image, filter_choice)

colours = input("if you have colours(yes/no): ")
if colours.lower() == 'yes':
    colour_tuple = getcolor()
    print(colour_tuple)

grey = input("if you have colour sepration(yes/no): ")
if grey.lower() == 'yes':
    grey_choice = int(input("enter the colour that you want:\n 1. Grey\n 2.Red\n 3. Green\n 4. Blue\n"))
    original_image = grey_pic(original_image,grey_choice)

original_image.show()