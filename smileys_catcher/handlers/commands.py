from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.handlers.callback_query import CallbackQueryHandler
from .utils import handle_like_reaction, handle_dislike_reaction, handle_ok_hand_reaction, \
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


@router.message(F.text == "👍")
async def handle_like_message(message: types.Message):
    response = handle_like_reaction()
    await message.answer(response)

@router.message(F.text == "👎")
async def handle_dislike_message(message: types.Message):
    response = handle_dislike_reaction()
    await message.answer(response)

@router.message(F.text == "👌")
async def handle_ok_hand_message(message: types.Message):
    response = handle_ok_hand_reaction()
    await message.answer(response)

@router.message(F.text == "🤣")
async def handle_rolling_on_the_floor_laughing_message(message: types.Message):
    response = handle_rolling_on_the_floor_laughing_reaction()
    await message.answer(response)


class LikeHandler(CallbackQueryHandler):
    async def handle(self) -> None:
        await self.event.message.answer("You have set 👍")
        await self.event.answer()

class DislikeHandler(CallbackQueryHandler):
    async def handle(self) -> None:
        await self.event.message.answer("You have set 👎")
        await self.event.answer()

class Ok_handHandler(CallbackQueryHandler):
    async def handle(self) -> None:
        await self.event.message.answer("You have set 👌")
        await self.event.answer()

class Rolling_on_the_floor_laughingHandler(CallbackQueryHandler):
    async def handle(self) -> None:
        await self.event.message.answer("You have set 🤣")
        await self.event.answer()


router.callback_query.register(LikeHandler, lambda c: c.data == 'like')
router.callback_query.register(DislikeHandler, lambda c: c.data == 'dislike')
router.callback_query.register(Ok_handHandler, lambda c: c.data == 'ok_hand')
router.callback_query.register(Rolling_on_the_floor_laughingHandler,
                               lambda c: c.data == 'rolling_on_the_floor_laughing')
