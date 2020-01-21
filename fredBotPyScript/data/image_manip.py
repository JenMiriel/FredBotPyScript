import pyautogui
from pathlib import Path
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import argparse
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'


def check_room(room_number):
    # take screenshot
    take_screenshot(room_number)
    # see if screenshot has robot / image manip
    # if no robot, is_clear = True; if robot, is_clear = False
    is_room_empty = compare_screens(room_number)
    return is_room_empty


def take_screenshot(room_number="office"):
    my_screenshot = pyautogui.screenshot()
    save_path = str(Path.cwd()) + "\\resources\\screens\\" + room_number + ".png"
    my_screenshot.save(save_path)


def compare_screens(room_number):
    # compare the images to the standard empty room
    are_images_similar = True

    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    # original = cv2.imread("images/jp_gates_original.png")
    # contrast = cv2.imread("images/jp_gates_contrast.png")
    original_room = cv2.imread("resources/screens/main_stage_original.png")
    # compare_room = cv2.imread("resources/compare.png")
    compare_room = cv2.imread("resources/screens/main_stage_original_modified.png")

    # convert the images to grayscale
    # original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # contrast = cv2.original_roomcvtColor(contrast, cv2.COLOR_BGR2GRAY)
    original_room = cv2.cvtColor(original_room, cv2.COLOR_BGR2GRAY)
    compare_room = cv2.cvtColor(compare_room, cv2.COLOR_BGR2GRAY)

    # initialize the figure
    # fig = plt.figure("Images")
    images = ("Original", original_room), ("Compare", compare_room)

    # # loop over the images
    # for (i, (name, image)) in enumerate(images):
    #     # show the image
    #     ax = fig.add_subplot(1, 3, i + 1)
    #     ax.set_title(name)
    #     plt.imshow(image, cmap=plt.cm.gray)
    #     plt.axis("off")
    #
    # # show the figure
    # plt.show()

    # compare the images
    # compare_images(original, original, "Original vs. Original")
    # compare_images(original, contrast, "Original vs. Contrast")
    are_images_similar = compare_images(original_room, compare_room, "Original vs. Compare")

    return are_images_similar


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the
    matched = False
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    # # setup the figure
    # fig = plt.figure(title)
    # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    #
    # # show first image
    # ax = fig.add_subplot(1, 2, 1)
    # plt.imshow(imageA, cmap=plt.cm.gray)
    # plt.axis("off")
    #
    # # show the second image
    # ax = fig.add_subplot(1, 2, 2)
    # plt.imshow(imageB, cmap=plt.cm.gray)
    # plt.axis("off")
    #
    # # show the images
    # plt.show()
    print("ssim value: ", s)

    if (s > .7) & (s <= 1):
        matched = True

    return matched


def find_text_in_image(orig_filename):
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=False,
                    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                    help="type of preprocessing to be done")
    ap.add_argument("-l", "--eng", help="language is english")
    args = vars(ap.parse_args())

    # load the example image and convert it to grayscale
    image = cv2.imread(orig_filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif args["preprocess"] == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    # show the output images
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)
    return text


