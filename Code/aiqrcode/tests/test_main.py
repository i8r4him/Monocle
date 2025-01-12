import unittest
from main import main
import os

class TestMain(unittest.TestCase):
    def test_main(self):
        message = "Test message"
        prompt = "Test prompt"
        main(message, prompt)
        self.assertTrue(os.path.exists("output/qr_code.png"))
        self.assertTrue(os.path.exists("export/generated_image.webp"))
        os.remove("output/qr_code.png")
        os.remove("export/generated_image.webp")

if __name__ == "__main__":
    unittest.main()