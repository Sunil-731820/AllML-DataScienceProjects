# OpenCV is a Python open-source library, which is used for computer vision in Artificial intelligence,
# Machine Learning, face recognition, etc.

# 1 : Writing the function to Read The Image From The Specified Locations and Displaying
import cv2
def readingTheImageFromSpecifiedLoactions():
    print("Start Of The Reading The image From The Specified Locations")
    img = cv2.imread(r'C:\Users\sunil\OneDrive\Pictures\PHOTO ONLY\imageiphone\CNNX2520.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(3)
    cv2.destroyAllWindows()
    print("After SuccessFully Read the image From The Specified Locations is ")

readingTheImageFromSpecifiedLoactions()

# Reading and Writing the Image to The Specified Loactions

def readingAndWritingImagefromSpecifiedLoactionAndWriting():
    print("The Start Of The Reading and Writing Of The Image From The Specified Loactions is ")
    # Reading The Image
    img = cv2.imread(r'C:\Users\sunil\OneDrive\Pictures\PHOTO ONLY\imageiphone\CNNX2520.jpg',1)
    # Saving The Image
    status = cv2.imwrite(r'C:\Users\sunil\OneDrive\Pictures\PHOTO ONLY\imageiphone\CNNX2520.jpg', 0, img)
    # status = cv2.imwrite(r'C:\Users\sunil\CNNX2520.jpg',0,img)
    print("The Status Of The Image After Saving " + status)

readingAndWritingImagefromSpecifiedLoactionAndWriting()