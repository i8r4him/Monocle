import unittest
from stable_diffusion_api import StableDiffusionAPI
from unittest.mock import patch, Mock


class TestStableDiffusionAPI(unittest.TestCase):
    @patch('stable_diffusion_api.requests.post')
    def test_generate_image(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'dummy_image_data'
        mock_post.return_value = mock_response

        api = StableDiffusionAPI(api_url="http://dummy_url", api_key="dummy_key")
        image_data = api.generate_image("Test prompt", "test_qr_code.png")

        self.assertEqual(image_data, b'dummy_image_data')


if __name__ == "__main__":
    unittest.main()
