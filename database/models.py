from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, DateTime, func


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
class Message:
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True )
    word: Mapped[str] = mapped_column(String(100), nullable = False)
    text: Mapped[str] = mapped_column(Text)
