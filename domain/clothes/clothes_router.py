from fastapi import APIRouter, File, UploadFile
import domain.clothes.clothes_service as service
from domain.s3.s3_service import upload_file

router = APIRouter(
    prefix="/fast/clothes",
)


@router.post("/check")
async def check_clothes(image: UploadFile = File(...)):
    # TODO: 의류 이미지 판별 로직
    is_clothes = True
    return {"isClothes": is_clothes}


@router.post("/rembg")
async def get_rembg_image(image: UploadFile = File(...)):
    url = await remove_background(image)
    return {"image": url}


@router.post("/rembg/info")
async def get_clothes_info(image: UploadFile = File(...)):
    # 배경 제거
    url = await remove_background(image)

    # 의류 정보 추출
    type = service.get_clothes_type(url)
    color = service.get_clothes_color(url)
    material = service.get_clothes_material(url)

    response = {
        "image": url,
        "type": type,
        "color": color,
        "material": material
    }
    return response


@router.post("/test")
async def check_clothes(image: UploadFile = File(...)):
    return upload_file(image)


async def remove_background(image):
    # 의류 이미지 배경 제거
    nobg_image = service.get_clothes_image(image)

    # s3에 배경 제거 이미지 업로드 후 반환
    # url = upload_file(nobg_image)
    # return url
    return "https://fitsta-bucket.s3.ap-northeast-2.amazonaws.com/123.png"