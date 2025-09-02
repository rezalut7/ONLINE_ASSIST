from __future__ import annotations
from datetime import datetime, date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, Float, Date, DateTime, Boolean, Text
from .db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(unique=True, index=True)
    role: Mapped[str] = mapped_column(String(16), default="client")  # client|coach|admin
    full_name: Mapped[str] = mapped_column(String(128), default="")
    gender: Mapped[str] = mapped_column(String(8), default="male")
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    height_cm: Mapped[int | None] = mapped_column(Integer, nullable=True)
    weight_kg: Mapped[float | None] = mapped_column(Float, nullable=True)
    activity_level: Mapped[str] = mapped_column(String(16), default="moderate")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    plans: Mapped[list['Plan']] = relationship(back_populates="user")
    checkins: Mapped[list['CheckIn']] = relationship(back_populates="user")

class Plan(Base):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    type: Mapped[str] = mapped_column(String(16))  # diet|workout
    title: Mapped[str] = mapped_column(String(128))
    payload_json: Mapped[str] = mapped_column(Text)  # JSON as string
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped['User'] = relationship(back_populates="plans")
