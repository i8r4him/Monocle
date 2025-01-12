import unittest
from qr_code_generator import QRCodeGenerator
import os

class TestQRCodeGenerator(unittest.TestCase):
    def test_generate_qr_code(self):
        qr_gen = QRCodeGenerator("Test data")
        output_path = "test_qr_code.png"
        qr_gen.generate_qr_code(output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)

if __name__ == "__main__":
    unittest.main()