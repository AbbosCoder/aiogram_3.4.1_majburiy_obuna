from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .database import HolderMiddleware
from .subscription import SubscriptionMiddleware


def setup(dp: Dispatcher, pool: sessionmaker):
    dp.update.middleware(HolderMiddleware(pool=pool))
    dp.message.middleware(SubscriptionMiddleware())
