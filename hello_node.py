print("✅ my_hello_node is being loaded!")

class HelloWorldNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "Piyush"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "say_hello"

    def say_hello(self, name):
        return (f"Hello, {name}!",)

NODE_CLASS_MAPPINGS = {
    "HelloWorld": HelloWorldNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HelloWorld": "👋 Hello World Node"
}
