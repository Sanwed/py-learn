from module13.api import api
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    address = State()

@dp.message_handler(text = 'Заказать')
async def buy(message):
    await message.answer('Send your address')
    await UserState.address.set()

@dp.message_handler(state = UserState.address)
async def fsm_handler(message, state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    await message.answer(f'Deliver will send to {data["first"]}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
