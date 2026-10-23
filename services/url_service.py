import secrets
import string

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import URL


class URLService:
    ALPHABET = string.ascii_letters + string.digits

    def generate_short_code(length: int = 6) -> str:
        return "".join(secrets.choice(URLService.ALPHABET) for _ in range(length))

    @staticmethod
    def create_short_url(*, db: Session, original_url: str) -> URL:
        attempts = 5

        for _ in range(attempts):
            short_code = URLService.generate_short_code()

            url_record = URL(original_url=original_url, short_code=short_code)
            db.add(url_record)

            try:
                db.commit()
                db.refresh(url_record)
                return url_record

            except IntegrityError:
                db.rollback()

        raise RuntimeError("Could not generate a unique short code.")
