from app.database import async_session_maker
from sqlalchemy import select

from app.booking.models import Bookings
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

