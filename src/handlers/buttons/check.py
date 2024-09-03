from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from typing import Union
from aiogram import Bot



async def check_user(channels: list, event: Message) -> InlineKeyboardMarkup:
    buttons = []
    
    for channel in channels:

        async def check(user_id, channel: Union[int, str]):
            try:
                chat_member = await event.bot.get_chat_member(channel, user_id)

                if chat_member.status in ['member', 'administrator', 'creator']:
                    return True
                else:
                    return False
            except Exception as e:
                
                print(f"Error checking member status: {e}")
                return False
            
        status = await check(user_id=event.from_user.id,channel=channel)

        if status!=True:
            chat = await event.bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            button = InlineKeyboardButton(text=f'➕ {chat.title}', url=invite_link)
            buttons.append([button])
    

    # Initialize InlineKeyboardMarkup with the inline_keyboard parameter
    kanal_obuna = InlineKeyboardMarkup(inline_keyboard=buttons)

    return kanal_obuna
