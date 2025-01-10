from fastapi import FastAPI
from typing import Optional

from fastapi.params import Query, Depends
from pydantic import BaseModel
from datetime import date

from app.booking.router import router as router_bookings


app = FastAPI()

app.include_router(router_bookings)


class HotelSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool]=None,
            stars: Optional[int]=Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get("/hotels")
def get_hotels(
        search_args: HotelSearchArgs = Depends()
):
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date



@app.post("/booking")
def add_booking(booking: SBooking):
    pass

# uvicorn app.main:app --reload
# result.mapping().all()