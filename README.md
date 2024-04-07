# TRUsteg
A modern steganography tool for securing messages and communications using a unique binary to LSB-bit methodology, that goes undetected from common analysis tools


TRUsteg is a steganography application designed to conceal and retrieve text messages within images. It utilizes steganographic techniques to embed hidden messages in the least significant bits of image pixels, ensuring the alterations are imperceptible to the naked eye. TRUsteg provides a user-friendly graphical interface, allowing users to easily load images, enter messages, and perform steganography operations with simple button clicks.

## Features

- Conceals text messages within images
- User-friendly GUI for intuitive interaction
- Encrypts hidden messages for enhanced security
- Utilizes steganographic techniques to ensure imperceptibility
- Supports hiding and retrieving messages from images

## Problem Statement

TRUsteg addresses the security challenge of transmitting sensitive information covertly over potentially insecure channels. By concealing messages within non-secret data like images, TRUsteg provides a discreet communication method. Additionally, the encryption of hidden messages ensures that even if discovered, the content remains unreadable without the decryption key.

## Learning Experience

Throughout the development of TRUsteg, valuable insights were gained into digital image processing, GUI development in Python, and steganographic techniques. The project also highlighted the importance of user experience design in software development, especially when dealing with complex technical concepts.

## Future Improvements

With more time, TRUsteg can be further improved in the following areas:
- Support for different image formats
- Integration of encryption algorithms for enhanced security
- Optimization for handling larger data payloads without compromising image quality

## Tech Stack

TRUsteg was developed using the following technologies:
- Python
- PIL (Python Imaging Library)
- Numpy
- Tkinter

## Challenges Faced

Balancing user-friendliness with technical robustness was a significant challenge during development. Handling different image sizes and formats, ensuring undetectability of embedded messages, and optimizing performance were some of the key challenges encountered.

## Inspiration

The inspiration for TRUsteg stemmed from the intriguing world of digital steganography – the art of hiding information in plain sight. In an era where data privacy and security are paramount, TRUsteg was created to provide a tool that not only secures information but does so in a simple and accessible manner.

## Why TRUsteg?

TRUsteg stands out for successfully integrating steganography algorithms into a user-friendly GUI. The application maintains the integrity and confidentiality of hidden messages while being accessible to users with no technical background in steganography.

## How to Use

To use TRUsteg, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python trusteg.py`.
4. Load an image, enter your message, and perform steganography operations using the provided interface.

## Acknowledgments

Special thanks to the developers of Python Imaging Library (PIL) and Tkinter for their invaluable contributions to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
