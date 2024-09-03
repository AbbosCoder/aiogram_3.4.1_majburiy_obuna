from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Any, Dict
from aiogram.types import Message
from src.handlers.buttons.check import check_user

class SubscriptionMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        channels = [
            "-1001833925242","-1001860917837"
        ]
        channel_statuses = []
        for channel in channels:
            status = await event.bot.get_chat_member(
                chat_id=channel,
                user_id=event.from_user.id
            )
            channel_statuses.append(status.status)
        if 'left' in channel_statuses:
            keyboard = await check_user(channels, event)
            await event.answer(
                text="Iltimos, barcha kanallarga obuna bo'ling!",
                reply_markup=keyboard
            )
        else:
            return await handler(event, data)
