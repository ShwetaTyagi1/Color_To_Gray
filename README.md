 **Image Conversion to Grayscale Using OpenCV**

## Overview:
This project demonstrates a simple Python script that allows users to convert any image into grayscale using OpenCV. Users can input an image path, view the converted grayscale image, and decide whether to save the output. The code is well-commented to enhance understanding.

## Features:
- Converts any image to grayscale.
- User can view the grayscale image before deciding to save it.
- The output image can be saved in a specified directory by pressing a key.
- Fully commented code for clarity.

## Technologies Used:
- **Python**: The core programming language.
- **OpenCV**: Library used for image processing operations.

## How to Use:

### Requirements:
- Python 3.x
- Required Python libraries:
    - `opencv-python`

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Image-Grayscale-Converter.git
   cd Image-Grayscale-Converter
   ```
2. Install the required dependency:
   ```bash
   pip install opencv-python
   ```

### Usage:
1. Run the script:
   ```bash
   python grayscale_converter.py
   ```

2. When prompted:
   - Enter the image file path (e.g., `C:\Users\YourUsername\Pictures\image.jpg`).

3. The grayscale version of the image will be displayed. You can press:
   - **'s'** to save the image (the image will be saved as `output.png` in the default location).
   - Any other key to close the window without saving the image.

### Example:
```bash
Enter path of the image and its name: C:\Users\YourUsername\Pictures\image.jpg
```

After the grayscale conversion, if you press 's', the image will be saved as `output.png` in the specified location.

---

## Contributing:
Feel free to contribute by submitting pull requests or reporting issues.



