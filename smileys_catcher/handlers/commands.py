from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import handle_like_reaction, handle_poo_reaction, handle_ok_hand_reaction, \
    handle_rolling_on_the_floor_laughing_reaction


router = Router()


@router.message(Command('start'))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👍", callback_data="like"),
         InlineKeyboardButton(text="👎", callback_data="dislike"),
         InlineKeyboardButton(text="👌", callback_data="ok_hand"),
         InlineKeyboardButton(text="🤣", callback_data="rolling_on_the_floor_laughing")]
    ])
    await message.answer("Hi! How do you feel about this message?", reply_markup=keyboard)


@router.message()
async def handle_text_message(message: types.Message):
    if "💩" in message.text:
        response = handle_poo_reaction()
        await message.answer(response)
    elif "👍" in message.text:
        response = handle_like_reaction()
        await message.answer(response)
    elif "👌" in message.text:
        response = handle_ok_hand_reaction()
        await message.answer(response)
    elif "🤣" in message.text:
        response = handle_rolling_on_the_floor_laughing_reaction()
        await message.answer(response)
