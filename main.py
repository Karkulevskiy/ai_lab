from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from io import BytesIO
from PIL import Image
import uvicorn

app = FastAPI()

@app.get("/test")
async def test():
    return Response(content="hello")

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # Открываем изображение
    image = Image.open(file.file)

    # Преобразуем в черно-белый формат
    image = image.convert("L")

    # Сохраняем в байтовый поток
    img_bytes = BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    return Response(content=img_bytes.getvalue(), media_type="image/png")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
