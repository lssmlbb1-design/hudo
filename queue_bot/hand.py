from aiogram import Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import OWNER_ID
from data import load_data, save_data
from key import USER_ACTIONS, SERVICES
from queue import QueueState, get_queue_position
from validators import validate_name

dp = Dispatcher()
user_states = {}

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=USER_ACTIONS["join_queue"])],
            [KeyboardButton(text=USER_ACTIONS["my_ticket"])],
            [KeyboardButton(text=USER_ACTIONS["cancel_ticket"])],
            [KeyboardButton(text=USER_ACTIONS["rules"])],
        ],
        resize_keyboard=True
    )

def services_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=s)] for s in SERVICES],
        resize_keyboard=True
    )

@dp.message(CommandStart())
async def cmd_start(m: types.Message):
    await m.answer(
        "Привет! Я бот очереди.\n"
        "Нажми «Записаться в очередь» чтобы начать.",
        reply_markup=main_keyboard()
    )

@dp.message(Command("admin"))
async def cmd_admin(m: types.Message):
    if m.from_user.id != OWNER_ID:
        await m.answer("Нет доступа.")
        return
    data = load_data()
    waiting = [e for e in data["entries"] if e["status"] == "waiting"]
    if not waiting:
        await m.answer("Очередь пуста.")
        return
    lines = [f"{e['id']}. {e['name']} — {e['service']}" for e in waiting]
    await m.answer("Очередь:\n" + "\n".join(lines))

@dp.message(Command("rules"))
async def cmd_rules(m: types.Message):
    await m.answer(
        "Правила:\n"
        "1. Один человек — одна запись.\n"
        "2. Отменить можно только свою запись.\n"
        "3. Приходи вовремя."
    )

# TODO: напиши handler для кнопки "Записаться в очередь"
# - покажи services_keyboard()
# - установи user_states[user_id] = {"state": QueueState.CHOOSING_SERVICE}
# @dp.message(F.text == USER_ACTIONS["join_queue"])

# TODO: напиши handler для выбора услуги
# - проверь что пользователь в состоянии CHOOSING_SERVICE
# - сохрани service в user_states[user_id]
# - переведи state в WAITING_NAME
# - попроси ввести имя

# TODO: напиши handler для ввода имени
# - проверь через validate_name()
# - если невалидно — попроси заново
# - если ок — покажи подтверждение

# TODO: напиши handler для подтверждения
# - создай entry: id = data["next_id"], telegram_user_id, name, service, status, created_at
# - добавь в data["entries"], next_id += 1
# - save_data(data)
# - покажи номер id и позицию через get_queue_position()

# TODO: напиши handler для "Моя запись"
# - найди entry пользователя со status == "waiting"
# - покажи имя, услугу, позицию

# TODO: напиши handler для отмены
# - найди entry пользователя
# - пометь status = "cancelled"
# - save_data(data)
