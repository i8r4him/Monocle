import requests
import json
import base64

class StableDiffusionAPI:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def generate_image(self, prompt: str, qr_code_path: str, controlnet_type: str = "openpose") -> bytes:
        with open(qr_code_path, "rb") as qr_code_file:
            control_image_data = base64.b64encode(qr_code_file.read()).decode('utf-8')

        payload = {
            "key": self.api_key,
            "controlnet_model": "qrcode,qrcode2",
            "controlnet_type": "qrcode",
            "model_id": "DPM++ 2M Karras",
            "auto_hint": "yes",
            "guess_mode": "yes",
            "prompt": prompt,
            "negative_prompt": None,
            "control_image": control_image_data,
            "init_image": None,
            "mask_image": None,
            "width": "512",
            "height": "512",
            "samples": "1",
            "scheduler": "UniPCMultistepScheduler",
            "num_inference_steps": "30",
            "safety_checker": "no",
            "enhance_prompt": "yes",
            "guidance_scale": 7.5,
            "controlnet_conditioning_scale": 0.7,
            "strength": 0.55,
            "lora_model": "yae-miko-genshin,more_details",
            "clip_skip": "2",
            "tomesd": "yes",
            "use_karras_sigmas": "yes",
            "vae": None,
            "lora_strength": None,
            "embeddings_model": None,
            "seed": None,
            "webhook": None,
            "track_id": None
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"API request failed: {response.json()}")

