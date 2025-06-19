from fastapi import FastAPI
from deepface import DeepFace
from pydantic import BaseModel
import base64
import requests
import tempfile
import mimetypes


api = FastAPI()

class FaceRequest(BaseModel):
    reference: str
    image: str

def base64_to_temp_image(base64_str: str, suffix=".jpg") -> str:
    try:
        if "," in base64_str:
            base64_str = base64_str.split(",")[-1]

        image_data = base64.b64decode(base64_str)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        temp_file.write(image_data)
        temp_file.close()

        return temp_file.name

    except Exception as e:
        raise ValueError(f"Failed to decode and save base64 image: {e}")


@api.post("/verify")
async def verify(data: FaceRequest):
    try:
        ref_img = base64_to_temp_image(data.reference)
        test_img = base64_to_temp_image(data.image)

        print({"ref": ref_img, "test": test_img})

        result = DeepFace.verify(img1_path=ref_img, img2_path=test_img, threshold=0.3)

        print({"result": result});

        return {
            "status_code": 200,
            "data": result
        }

    except Exception as e:
        return {
            "status_code": 400,
            "data": str(e)
        }