
from PIL import Image
import os
import folder_paths
import numpy as np
import torch

class LoadImageNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_path": ("STRING", {
                    "multiline": False,
                    "default": ""
                })
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "load_image"

    CATEGORY = "Custom/Image"

    def load_image(self, image_path):
        full_path = os.path.join(folder_paths.base_path, image_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Image not found at: {full_path}")
        
        img = Image.open(full_path).convert("RGB")
        img = np.array(img).astype(np.float32) / 255.0  # Normalize to 0–1
        img = torch.from_numpy(img).unsqueeze(0)  # Add batch dimension: [1, H, W, C]
        img = img.permute(0, 3, 1, 2)  # Rearrange to [B, C, H, W]
        return (img,)

NODE_CLASS_MAPPINGS = {
    "LoadImageNode": LoadImageNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageNode": "🖼️ Load Image (Custom)",
}
