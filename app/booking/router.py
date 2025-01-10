from fastapi import APIRouter
from app.booking.dao import BookingDAO
from app.booking.schemas import SBooking

router = APIRouter(
    prefix="/booking",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking() -> list[SBooking]:
    return await BookingDAO.find_all()

