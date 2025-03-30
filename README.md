# Python Turtle Hearts

Celebrate Valentine's Day with a unique, coded gift using Python's Turtle graphics. This script creates a hypnotizing animation that culminates in a warm message, offering a creative way to express your affection.

## Overview

The script uses Python's Turtle module to draw a dynamic background very slowly, which only accumulates the feeling of joy while waiting for the main part. followed by a series of heart shapes and a customizable message.

## Features

- **Gradient Background**: A double-gradient effect achieved by blending two color ranges, creating a visually appealing backdrop.
- **Heart Shapes**: Sequentially drawn hearts that symbolize your feelings.
- **Customizable Message**: Personalize the final text on the heart shapes to address the message.

## Customization Guide

To change the script to your preferences, consider adjusting the following parameters:

- **Gradient Colors**: Modify the `colors_1` and `colors_2` variables to change the gradient hues. Each represents a color range in HSV format.

  ```python
  colors_1 = color_range((0.56, 0, 1), (0.56, 0, 0.88), 20)
  colors_2 = color_range((0.56, 0, 0.88), (0.6, 0.47, 1), 20)
  ```

- **Gradient Visibility**: Alter the `step` value in the `color_range` function to adjust the gradient's prominence. A smaller step increases gradient visibility.

  ```python
  step = [(end_rgb[i] - start_rgb[i]) / (n-1) for i in range(3)]
  ```

- **Drawing Speed**: Set the Turtle's speed using `turtle.speed()`. The maximum speed is 0.

  ```python
  turtle.speed(0)
  ```

- **Cursor Shape and Size**: Change the Turtle's appearance with `turtle.shape()` and `turtle.shapesize()`.

  ```python
  turtle.shape("turtle")
  turtle.shapesize(2, 2)
  ```

- **Colors of Shapes and Text**: Customize the colors of the hearts and text by adjusting the `turtle.color()` parameters.

  ```python
  turtle.color((0, 0.29, 0.29), (0.85, 0.2, 0.53))  # Contour and fill colors
  ```

- **Text Content and Font**: Personalize the message and its appearance by modifying the `draw_text` function call. (most important customization part, please do not forget)

  ```python
  draw_text('Your custom text\n❤️')
  ```

## Usage

1. **Install Python**: Ensure Python is installed on your system.
2. **Run the Script**: Execute the script in a Python environment that supports Turtle graphics.
3. **Enjoy the Animation**: Watch as the background and hearts are drawn, culminating in your personalized message.

## Sample Output

For a preview of the final animation, refer to the `Sample` file included in this repository.

## Upcoming Versions

Future iterations of this script may include:

- **Faster Rendering**: An option to bypass the gradual drawing for an immediate display.
- **Enhanced Customization**: Additional parameters for more personalized animations.

## Acknowledgments

Thank you for exploring this creative coding project. I wish you lots of joy and hope, that it will impress you and your loved one this Valentine's Day.

#### Remarks
> This project is pure open-source and you are free to use it
> If you encounter bugs or have suggestions, please let me know via a descriptive pull request
