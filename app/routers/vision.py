from fastapi import APIRouter, File, UploadFile
from schemas import FaceRecognitionResponse, ProductClassificationResponse
from services.cv_service import cv_service

router = APIRouter()

@router.post("/recognize-face", response_model=FaceRecognitionResponse)
async def recognize_face(file: UploadFile = File(...)):
    image_bytes = await file.read()
    return cv_service.recognize_face(image_bytes)

@router.post("/classify-product", response_model=ProductClassificationResponse)
async def classify_product(file: UploadFile = File(...)):
    image_bytes = await file.read()
    return cv_service.classify_product(image_bytes)
