# Monocle Glass QR Code Identifier

This project is a collaborative university initiative involving 5 team members. The monocle glass, provided as raw hardware with a base library, was programmed by our team to identify QR codes hidden in AI-generated art. The decoded results are displayed directly on the monocle glass, enabling a unique augmented reality experience.

---

## Features

1. **Custom QR Code Recognition**
   - Designed from scratch to detect and decode QR codes embedded in complex AI-generated art.
   - Overcomes challenges such as distortions and artistic patterns to accurately extract the QR code.

2. **Real-Time Processing**
   - Efficiently scans images using the monocle’s integrated camera.
   - Decodes the QR code and immediately projects the result onto the monocle’s display.

3. **Software-Only Development**
   - The monocle glass hardware came with a raw factory setup and a basic library.
   - Our team programmed all the functionality, including QR code recognition, data decoding, and result display.

4. **AI Art Compatibility**
   - Optimized to detect QR codes hidden within AI-generated patterns and images.

---

## Technologies Used

### Hardware
- **Monocle Glass**: Raw factory-issued hardware with integrated display and camera.
- **Library**: Provided factory library for interfacing with the hardware.

### Software
- **Python**:
  - Used for QR code recognition with libraries like `opencv` and `pyzbar`.
  - Developed algorithms to adapt recognition to complex artistic patterns.
- **Monocle Library**: Customized usage of the factory-provided library for hardware integration.
- **AI Art Tools**:
  - Created custom AI art with hidden QR codes using tools like DALL·E or MidJourney.

---

## Installation

### Prerequisites
1. A factory monocle glass device.
2. Python 3.x installed on your development system.
3. Install the required Python libraries:
   ```bash
   pip install opencv-python pyzbar
