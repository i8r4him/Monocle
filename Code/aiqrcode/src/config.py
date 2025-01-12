import os

class Config:
    API_URL = os.getenv('API_URL', 'https://192.168.178.21')
    API_KEY = os.getenv('API_KEY', '123456')
    OUTPUT_QR_PATH = os.getenv('OUTPUT_QR_PATH', 'export/qr_code.png')
    EXPORT_IMAGE_PATH = os.getenv('EXPORT_IMAGE_PATH', 'export/generated_image.jpeg')
    CONTROLNET_TYPE = os.getenv('CONTROLNET_TYPE', 'qrcode')