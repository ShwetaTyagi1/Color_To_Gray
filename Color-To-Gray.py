
import cv2 #openCV used as cv2 in python

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
