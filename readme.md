# Color Detection with OpenCV

This Python script uses OpenCV to perform color detection in real-time using your webcam. It detects and tracks objects of specific colors defined in the HSV color space and draws rectangles around them.

## Requirements

- Python 3.x
- OpenCV library (you can install it using `pip install opencv-python`)
- A webcam

## How to Use

1. Run the `main.py` script.

2. The script will use your webcam to capture real-time video input.

3. It will detect objects of specific colors (e.g., red, green, blue) based on the predefined HSV color ranges in the `color_ranges` dictionary.

4. Detected objects will be outlined with rectangles, and the color name will be displayed on top of them.

5. Press the 'q' key to exit the program.

## Customization

You can customize the colors to detect by modifying the `color_ranges` dictionary. Each color is defined by its lower and upper HSV range.

Example:
```python
color_ranges = {
    'red': ([100, 50, 50], [255, 100, 100]),
    'green': ([50, 100, 50], [100, 255, 100]),
    'blue': ([50, 50, 100], [100, 100, 255])
}