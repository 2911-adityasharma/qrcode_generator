QR Code Generator

This Python script generates a dynamic QR code based on a provided URL. The QR code is saved as an image file, and its version (size and capacity) is randomly selected each time the script runs.

Features

Generates a QR code with a randomly selected version (1 to 23).
QR code data can be customized (e.g., a URL).
Saves the generated QR code as an image file.
Uses the qrcode library for QR code generation and random for randomization of the QR code version.
Prerequisites
Before running the script, ensure you have Python installed on your system. You'll also need to install the following Python libraries:

qrcode: A library for generating QR codes.
To install the necessary libraries, use the following command:

bash
Copy
pip install qrcode[pil]
pil is included to ensure that image generation is supported.

How to Use

Clone or download this repository.
Open a terminal/command prompt in the project directory.
Run the script:
bash
Copy
python generate_qr_code.py
This will generate a QR code for the URL https://www.youtube.com and save it as qrcode.png.

You can modify the data variable in the script to generate a QR code for any other URL or text.

Customization

Change the URL: Modify the data variable in the script to any URL or text that you want to encode into the QR code.
Adjust Image Settings: You can tweak the box_size, border, and error_correction settings in the script to modify the appearance and error correction level of the generated QR code.
Randomized QR Code Version: The QR code's version (size and capacity) is randomly chosen between versions 1 and 23, which affects the QR code's overall size.
Example
Running the script will generate a file named qrcode.png that contains a QR code linking to https://www.youtube.com.

License
This project is licensed under the MIT License - see the LICENSE file for details.
