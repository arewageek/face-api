from fastapi import FastAPI
from deepface import DeepFace
from pydantic import BaseModel
import base64
import tempfile


api = FastAPI()

class Verify(BaseModel):
    reference: str
    photo: str


def decode(base64_str: str, suffix=".jpg") -> str:
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
async def verify(data: Verify):
    try:
        reference = decode(data.reference)
        photo = decode(data.photo)

        result = DeepFace.verify(img1_path=reference, img2_path=photo, threshold=0.4)

        print({"result": result});

        return {
            "status": "success",
            "satus_code": 200,
            "data": result
        }

    except Exception as e:
        return {
            "status": "error",
            "status_code": 400,
            "data": str(e)
        }

            "status_code": 400,
            "data": str(e)
        }