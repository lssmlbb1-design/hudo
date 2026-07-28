from aiogram import Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import OWNER_ID
from data import load_workouts, save_workouts
from key import MAIN_MENU
from statistics import calculate_volume, calculate_pace, get_recent_workouts, get_max_weight
from validators import parse_positive_int, parse_positive_float

dp = Dispatcher()
user_states = {}

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=MAIN_MENU["add_workout"])],
            [KeyboardButton(text=MAIN_MENU["history"])],
            [KeyboardButton(text=MAIN_MENU["stats"])],
            [KeyboardButton(text=MAIN_MENU["goals"])],
        ],
        resize_keyboard=True
    )

@dp.message(CommandStart())
async def cmd_start(m: types.Message):
    await m.answer(
        "Привет! Я бот тренировок.\n"
        "Записывай свои тренировки и смотри прогресс.",
        reply_markup=main_keyboard()
    )

# TODO: напиши handler для "Добавить тренировку"
# - спроси тип: силовая или бег
# - сохрани user_states[user_id] = {"state": "choosing_type"}
# @dp.message(F.text == MAIN_MENU["add_workout"])

# TODO: напиши handler для ввода упражнения
# - для силовой: спроси подходы, повторения, вес
# - для бега: спроси дистанцию и время

# TODO: напиши handler для ввода чисел
# - проверь через parse_positive_int / parse_positive_float
# - если плохое — попроси заново

# TODO: напиши handler для сохранения
# - создай запись, добавь в data["workouts"]
# - save_workouts(data)
# - покажи объём (calculate_volume) или темп (calculate_pace)

# TODO: напиши handler для "Моя история"
# - get_recent_workouts(data["workouts"], limit=5)
# - покажи список

# TODO: напиши handler для "Статистика недели"
# - отфильтруй тренировки за 7 дней
# - покажи количество, общий объём, лучший вес через get_max_weight()
