import cv2 as cv

from CommentGenerator.models.FacialFeaturesModel import FacialFeaturesModel
from global_variables import PATH_TO_IMAGES, IMAGE_SIZE
from fer import FER


def show_random_images(n=10):
    for i in range(n):
        img_str = '000001.jpg'
        img = cv.imread(PATH_TO_IMAGES + img_str)
        print(img)
        print(type(img))
        print(img.shape)

        cv.imshow("Display window", img)
        k = cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == '__main__':
    img_str = '000034.jpg'
    img = cv.imread(PATH_TO_IMAGES + img_str)
    img = cv.resize(img, IMAGE_SIZE)
    print(img)
    print(type(img))
    print(img.shape)

    cv.imshow("Display window", img)

    ffm = FacialFeaturesModel()
    print(ffm.predict(img))

    k = cv.waitKey(0)
    cv.destroyAllWindows()
