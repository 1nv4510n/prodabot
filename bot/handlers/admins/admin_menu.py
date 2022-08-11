from aiogram import Router
from aiogram.types import Message, CallbackQuery

from bot.config import config
from bot.filters.admin_filter import AdminFilter

from .mass_mailing import router as mailing_router
from .statistics import router as stats_router

from bot.keyboards.admin_keyboard import make_admin_menu_keyboard

router = Router()
router.include_router(mailing_router)
router.include_router(stats_router)
router.message.filter(AdminFilter(admin_id=config.admin_id))
router.callback_query.filter(AdminFilter(admin_id=config.admin_id))

@router.message(commands=['admin'])
async def admin_menu_handler(message: Message) -> None:
    await message.answer('Выберите действие', reply_markup=make_admin_menu_keyboard())
    
@router.callback_query(text='exit_menu')
async def exit_menu_callback(call: CallbackQuery) -> None:
    await call.answer(text='Успешно')
    await call.message.delete()
    
@router.callback_query(text='back_menu')
async def back_menu_callback(call: CallbackQuery) -> None:
    await call.message.edit_text(text='Выберите действие', reply_markup=make_admin_menu_keyboard())