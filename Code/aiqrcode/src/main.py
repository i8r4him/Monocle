from qr_code_generator import QRCodeGenerator
from stable_diffusion_api import StableDiffusionAPI
from config import Config
from utils import save_image, create_output_directory, create_export_directory

def main(message: str, prompt: str) -> None:
    create_output_directory('output')
    create_export_directory('export')

    # Step 1: Generate QR Code
    qr_generator = QRCodeGenerator(data=message)
    qr_generator.generate_qr_code(Config.OUTPUT_QR_PATH)
    print(f"QR Code generated at {Config.OUTPUT_QR_PATH}")

    # Step 2: Generate Image using Stable Diffusion API with ControlNet
    stable_diffusion_api = StableDiffusionAPI(api_url=Config.API_URL, api_key=Config.API_KEY)
    image_data = stable_diffusion_api.generate_image(
        prompt=prompt,
        qr_code_path=Config.OUTPUT_QR_PATH,
        controlnet_type=Config.CONTROLNET_TYPE
    )
    save_image(image_data, Config.EXPORT_IMAGE_PATH)
    print(f"Generated image saved at {Config.EXPORT_IMAGE_PATH}")

if __name__ == "__main__":
    message = "Your message here"
    prompt = "Your prompt here"
    main(message, prompt)
