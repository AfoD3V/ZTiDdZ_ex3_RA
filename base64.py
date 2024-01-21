import base64

def encode_base64(text: str) -> str:
    return base64.b64encode((text).encode('utf-8')).decode('utf-8')


def decode_base64(text: str) -> str:
    return base64.b64decode((text).encode('utf-8')).decode('utf-8')


text_to_code = "Hello World"
print(f"Encoded text: {encode_base64(text_to_code)}")
print(f"Decoded text: {decode_base64(encode_base64(text_to_code))}")