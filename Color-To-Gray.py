
import cv2 #openCV used as cv2 in python
"""
img1=cv2.imread("C:\\Users\\Shweta Tyagi\\OneDrive\\Pictures\\user.jpg") #imread function is used to take input in form of an image from any location on the system
#using \\ or / incase of \ because of unicode error
#imread takes two parameter-location, 0/1/-1 0-returns a grayscale img, 1 returns colourful image , -1-unchanged ie same as original image but just with a litle higher saturation , default = 1  
img1=cv2.resize(img1, (800,800)) #(width,height)  resized image so it opens of a particular size in the new window 
print(img1)
cv2.imshow("original", img1) #original is the name i gave to the new window in which the image img1 will open
cv2.waitKey() #default arg = 0 ie indefinite static window, else we can give number of milliseconds
cv2.destroyAllWindows() #after code terminates, all windows will be destroyed
"""

# Project: Image conversion to grayscale

# Took input from user
path = input("Enter path of the image and its name: ")
print("Your path:", path)

# Read
img2 = cv2.imread(path, 0)  # 0 as I want to convert to grayscale
img2 = cv2.resize(img2, (550, 550))

# First show the converted img to the user
cv2.imshow("output", img2)

# Now, if user presses 's' then img saves else it destroys all windows and exits 
k = cv2.waitKey(0)  # Registers whatever key's ascii value that user presses while img being displayed
if k == ord("s"):
    # Change the output path to a writable directory
    cv2.imwrite(r"C:\Users\Shweta Tyagi\output.png", img2)  #using r before path to adhere to unicode
    cv2.destroyAllWindows()
    print("Image saved as output.png in users directory.")
else: 
    cv2.destroyAllWindows()