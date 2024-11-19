from api import api
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from module14.crud_functions import initiate_db, get_all_products

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()

reply_kb = ReplyKeyboardMarkup(
  keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')]
  ],
  resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
  ]
)

menu = InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
  ]
)


class UserState(StatesGroup):
  age = State()
  growth = State()
  weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
  await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=reply_kb)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
  products = get_all_products()
  for product in products:
    await message.answer_photo(
      photo='https://i.ibb.co/G7VZVws/14.jpg',
      caption=f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} руб.')
  await message.answer('Выберите продукт для покупки:', reply_markup=menu)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
  await message.answer('Выберите опцию', reply_markup=inline_kb)


@dp.message_handler()
async def all_messages(message):
  await message.answer('Введите команду /start, чтобы начать общение.')


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
  await call.message.answer(
    'Упрощенный вариант формулы Миффлина-Сан Жеора: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
  await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
  await call.message.answer('Введите свой возраст')
  await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
  await state.update_data(age=message.text)
  await message.answer('Введите свой рост')
  await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
  await state.update_data(growth=message.text)
  await message.answer('Введите свой вес')
  await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
  await state.update_data(weight=message.text)
  data = await state.get_data()
  calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
  await message.answer(f'Необходимое количество калорий в сутки: {calories}')
  await state.finish()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
  await call.message.answer('Вы успешно приобрели продукт!')
  await call.answer()


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
