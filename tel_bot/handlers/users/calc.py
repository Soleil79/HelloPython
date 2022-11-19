from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, logger
from keyboards.inline.choice_buttons import choice
from keyboards.inline.callback_datas import actions_callback
from module_calc import *

operator = {"+": sum_data, "-": sub_data, "*": mul_data, "/": div_data}

txt = ""

@dp.message_handler(Command("start")) # @ декоратор, dp - dispatcher, message_handler - работает с коммандами
async def ShowButtons(message: Message):
    await message.answer("Выполните действие", reply_markup=choice)

@dp.callback_query_handler(text_contains="C") #callback_query_handler - функция обратной связи, при нажатии на клавиши пользователем
async def DeleteButton(call: CallbackQuery):
    global txt
    txt = ""
    await call.message.edit_text("0", reply_markup=choice)


@dp.callback_query_handler(text_contains="<") 
async def BackSpaceButton(call: CallbackQuery):
    global txt
    if txt:
        txt = txt[:-1]
        if not txt:
            await call.message.edit_text("0", reply_markup=choice)
        await call.message.edit_text(f"{txt}", reply_markup=choice)
    else:
        await call.answer(cache_time=15)

@dp.callback_query_handler(text_contains="=") 
async def Result(call: CallbackQuery):
    global txt
    if txt:
        elements = txt.split()
        if len(elements) > 1:
            temp = [float(i) if "." in i else int(i) if i.replace(".", "").isdigit() else i for i in elements]
            while len(temp)>1:
                a, b, c = temp[:3]
                temp[:3] = [operator[b](a,c)]
        await call.message.edit_text(f"{txt} = {temp[0]}", reply_markup=choice)
        logger.debug(f"Результат = {temp[0]}")
        txt = ""
    else:
        await call.message.edit_text(f"Введите значение", reply_markup=choice)
        

@dp.callback_query_handler(actions_callback.filter())
async def Combine(call: CallbackQuery, callback_data: dict):
    global txt
    data = callback_data["item_name"]
    if data in "+-/*":
        txt += f" {data} " 
    else:
        txt += data
    await call.message.edit_text(f"{txt}", reply_markup=choice)
    logger.debug(f"Пользователь ввел: {txt}")


