from typing import Optional

from pydantic import BaseModel


class MovieSearch(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
    person_name: Optional[str] = None
    type: Optional[str] = None
