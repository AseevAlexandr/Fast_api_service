from fastapi import APIRouter


router = APIRouter(
    prefix="/booking",
    tags=["Бронирование"]
)


@router.get("")
def get_booking():
    pass


@router.get("{booking_id}")
def get_booking2(booking_id):
    pass

# uvicorn app.main:app --reload
# result.mapping().all()