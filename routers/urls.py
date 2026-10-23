from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import URLCreate, URLResponse
from services.url_service import URLService

router = APIRouter(prefix="/api/v1/urls", tags=["URLs"])


@router.post("", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def create_short_url_view(
    payload: URLCreate, request: Request, db: Session = Depends(get_db)
):
    original_url = str(payload.url)

    url_record = URLService.create_short_url(db=db, original_url=original_url)

    base_url = str(request.base_url).rstrip("/")
    short_url = f"{base_url}/{url_record.short_code}"

    return URLResponse(
        original_url=url_record.original_url,
        short_code=url_record.short_code,
        short_url=short_url,
    )
