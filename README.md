Monocle Glass QR Code Identifier

This project is a collaborative university initiative involving 5 team members. The monocle glass, provided as raw hardware with a base library, was programmed by our team to identify QR codes hidden in AI-generated art. The decoded results are displayed directly on the monocle glass, enabling a unique augmented reality experience.

Features
	1.	Custom QR Code Recognition
	•	Designed from scratch to detect and decode QR codes embedded in complex AI-generated art.
	•	Overcomes challenges such as distortions and artistic patterns to accurately extract the QR code.
	2.	Real-Time Processing
	•	Efficiently scans images using the monocle’s integrated camera.
	•	Decodes the QR code and immediately projects the result onto the monocle’s display.
	3.	Software-Only Development
	•	The monocle glass hardware came with a raw factory setup and a basic library.
	•	Our team programmed all the functionality, including QR code recognition, data decoding, and result display.
	4.	AI Art Compatibility
	•	Optimized to detect QR codes hidden within AI-generated patterns and images.

Technologies Used

Hardware
	•	Monocle Glass: Raw factory-issued hardware with integrated display and camera.
	•	Library: Provided factory library for interfacing with the hardware.

Software
	•	Python:
	•	Used for QR code recognition with libraries like opencv and pyzbar.
	•	Developed algorithms to adapt recognition to complex artistic patterns.
	•	Monocle Library: Customized usage of the factory-provided library for hardware integration.
	•	AI Art Tools:
	•	Created custom AI art with hidden QR codes using tools like DALL·E or MidJourney.

Installation

Prerequisites
	1.	A factory monocle glass device.
	2.	Python 3.x installed on your development system.
	3.	Install the required Python libraries:

pip install opencv-python pyzbar


	4.	Include the monocle library provided by the manufacturer.

Steps
	1.	Clone the repository:

git clone https://github.com/i8r4him/monocle-glass-qr.git


	2.	Connect the monocle glass to your development machine.
	3.	Install and configure the monocle library.
	4.	Run the QR code detection script:

python qr_scanner.py


	5.	View an AI-generated image with a hidden QR code through the monocle glass.

Workflow
	1.	Programming the Glass:
	•	Integrated the monocle library to enable camera functionality and display output.
	2.	QR Code Detection:
	•	Used Python and computer vision techniques to identify and decode QR codes.
	3.	AI Art:
	•	Generated creative AI art embedding QR codes for testing the system.
	4.	Result Display:
	•	Displayed decoded data directly on the monocle glass for a hands-free experience.

Challenges
	•	Programming the monocle glass from its raw factory setup.
	•	Adapting QR code recognition to artistic patterns and distorted designs.
	•	Real-time performance optimization within hardware constraints.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
	•	TU Braunschweig for providing resources and the monocle hardware.
	•	Open-source libraries (opencv, pyzbar) for enabling computer vision.
	•	AI art tools for creating unique test images.

What Works Well:
	1.	Clarity: The purpose and functionality of the project are explained in a way that’s easy to understand.
	2.	Detailed Features: You’ve highlighted all the key technical achievements of the project.
	3.	Acknowledgments: Crediting TU Braunschweig and open-source libraries is great for transparency.

Suggestions for Improvement:
	1.	Screenshots or Media: If possible, include images or videos showcasing:
	•	The monocle glass in action.
	•	Sample AI-generated art with QR codes.
	•	The results displayed on the monocle glass.
This will help readers visualize the project.
	2.	Future Work: Add a “Future Improvements” section to describe potential enhancements, such as:
	•	Optimizing QR code detection for faster processing.
	•	Extending compatibility with other AR devices.
	•	Adding support for other types of hidden data.
	3.	Consistent Formatting: Avoid bullets inside bullet points (e.g., under “Python”). Instead, use lists or paragraphs for sub-details.
