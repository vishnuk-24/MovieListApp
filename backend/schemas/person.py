from typing import Optional

from pydantic import BaseModel


class PersonSearch(BaseModel):
    name: Optional[str] = None
    movie_title: Optional[str] = None
    profession: Optional[str] = None
