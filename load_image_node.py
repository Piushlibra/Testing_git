from PIL import Image
import os

class LoadImageNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_path": ("STRING", {
                    "multiline": False,
                    "default": "path/to/your/image.jpg"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load"
    CATEGORY = "image"

    def load(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at: {image_path}")
        
        image = Image.open(image_path).convert("RGB")
        return (image,)

NODE_CLASS_MAPPINGS = {
    "LoadImageNode": LoadImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageNode": "Load Image from Path"
}
