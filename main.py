from aiogram import Dispatcher, types, F, filters, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()

class Card(StatesGroup):
    card_number = State()

main_button = ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт📚", request_contact=True)]
], resize_keyboard=True)

bot = Bot(token="7108432207:AAHLJoSoQW11pjL4pN2N9Bp4jrbt68KvrVc")
dp = Dispatcher(bot=bot)

keyboard1 = [
    [KeyboardButton(text="Til tallang🇺🇿, Выберите язык🇷🇺")]
]

keyboard2 = [
    [KeyboardButton(text="Kurs📕"), KeyboardButton(text="Karzina🛒"), KeyboardButton(text="Biz haqimizda📁")],
    [KeyboardButton(text="Yordam🚚"), KeyboardButton(text="Til o'zgartirish🏴"), KeyboardButton(text="Karzina")]
]

keyboard3 = [
    [KeyboardButton(text="Uzbek Tili🇺🇿"),KeyboardButton(text="Rus Tili🇷🇺")],
]

keyboard4 = [
    [KeyboardButton(text="Back-end📕"),
     KeyboardButton(text="Front-end📕"),
     KeyboardButton(text="Starter📕")],
    [KeyboardButton(text="Pro📕"),
     KeyboardButton(text="Design📕"),
     KeyboardButton(text="Edit Video📕")]
]

button_1 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="1"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

button_2 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="2"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

button_3 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="3"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

button_4 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="4"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

button_5 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="5"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

button_6 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="6"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

keyboard5 = [
    [KeyboardButton(text="UzCard💳"),KeyboardButton(text="Humo💳")],
]

button_7 = [
    [InlineKeyboardButton(text="Sayt",  url="https://space.marsit.uz/"  , callback_data="sayt"),
     InlineKeyboardButton(text="Video", url="https://youtu.be/5h1d3KwfOJM",callback_data="olmaslik2")]
]
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

rus1 = [
    [KeyboardButton(text="Курс📕"), KeyboardButton(text="Карзина🛒"), KeyboardButton(text="о нас📁")],
    [KeyboardButton(text="помощь🚚"), KeyboardButton(text="изменить язык🏴"), KeyboardButton(text="Karzina")]
]
rus2 = [
    [KeyboardButton(text="Back-enD📕"),
     KeyboardButton(text="Front-enD📕"),
     KeyboardButton(text="StarteR📕")],
    [KeyboardButton(text="PrO📕"),
     KeyboardButton(text="DesigN📕"),
     KeyboardButton(text="Edit VideO📕"),
     KeyboardButton(text="назад")]
]

rusbutton1 = [
    [InlineKeyboardButton(text="Купить", callback_data="rus1b"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

rusbutton2 = [
    [InlineKeyboardButton(text="Купить", callback_data="rus2b"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

rusbutton3 = [
    [InlineKeyboardButton(text="Купить", callback_data="rus3b"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

rusbutton4 = [
    [InlineKeyboardButton(text="Купить", callback_data="rus4b"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

rusbutton5 = [
    [InlineKeyboardButton(text="Купить", callback_data="rus5b"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

rusbutton6 = [
    [InlineKeyboardButton(text="Купить", callback_data="rus6b"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

rus3 = [
    [KeyboardButton(text="UzCarD💳"),KeyboardButton(text="HumO💳")],
]

rus4 = [
    [InlineKeyboardButton(text="Cайт",  url="https://space.marsit.uz/"  , callback_data="Cайт"),
     InlineKeyboardButton(text="Bu video",  url="https://youtu.be/5h1d3KwfOJM", callback_data="olmaslik1")]
]


Karzina=[]
button1 = InlineKeyboardMarkup(inline_keyboard=button_1)
button2 = InlineKeyboardMarkup(inline_keyboard=button_2)
button3 = InlineKeyboardMarkup(inline_keyboard=button_3)
button4 = InlineKeyboardMarkup(inline_keyboard=button_4)
button5 = InlineKeyboardMarkup(inline_keyboard=button_5)
button6 = InlineKeyboardMarkup(inline_keyboard=button_6)
button7 = InlineKeyboardMarkup(inline_keyboard=button_7)

main_button1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
main_button2 = ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
main_button3 = ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)
main_button4 = ReplyKeyboardMarkup(keyboard=keyboard4, resize_keyboard=True)
main_button5 = ReplyKeyboardMarkup(keyboard=keyboard5, resize_keyboard=True)
###################################################################################
###################################################################################
###################################################################################
main_rus1 = ReplyKeyboardMarkup(keyboard=rus1, resize_keyboard=True)
main_rus2 = ReplyKeyboardMarkup(keyboard=rus2, resize_keyboard=True)
main_rus3 = ReplyKeyboardMarkup(keyboard=rus3, resize_keyboard=True)

main_rusbutton1 = InlineKeyboardMarkup(inline_keyboard=rusbutton1)
main_rusbutton2 = InlineKeyboardMarkup(inline_keyboard=rusbutton2)
main_rusbutton3 = InlineKeyboardMarkup(inline_keyboard=rusbutton3)
main_rusbutton4 = InlineKeyboardMarkup(inline_keyboard=rusbutton4)
main_rusbutton5 = InlineKeyboardMarkup(inline_keyboard=rusbutton5)
main_rusbutton6 = InlineKeyboardMarkup(inline_keyboard=rusbutton6)
sayt = InlineKeyboardMarkup(inline_keyboard=rus4)



@dp.message(filters.Command("start"))
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Salom!\n Bizning Botimizga"
                         " Xush kelibsiz!\nKurs Soti"
                         "b oling va!, ismingizni kir"
                         "ting",)

@dp.message(Registration.first_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Familiyaniizni Kirting")

@dp.message(Registration.last_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer("Nomer Kiriting",reply_markup=main_button)

@dp.message(Registration.phone_number)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Имя: {data["first_name"]}\nФамилия: "
                         f"{data["last_name"]}\nНомер телефона: {data["phone_number"]}",
                         reply_markup=main_button1)
    await state.clear()

@dp.message(F.text == "Til tallang🇺🇿, Выберите язык🇷🇺")
async def start_function(message: types.Message):
    await message.answer("Siz Til Tallshingiz kerak!", reply_markup=main_button3)

@dp.message(F.text == "Back")
async def start_function(message: types.Message):
    await message.answer("Siz orqaga qaytingz!", reply_markup=main_button2)

@dp.message(F.text == "назад")
async def start_function(message: types.Message):
    await message.answer("вы вернулись назад", )

@dp.message(F.text == "Отправить контакт📚")
async def start_function(message: types.Message):
    await message.answer("siz kontankt tshildingiz", reply_markup=main_button1)

@dp.message(F.text == "Uzbek Tili🇺🇿")
async def start_function(message: types.Message):
    await message.answer("Siz Uzbek Tilini talladingiz!", reply_markup=main_button2)

@dp.message(F.text == "Rus Tili🇷🇺")
async def start_function(message: types.Message):
    await message.answer("Siz Rus Tilini talladingiz!", reply_markup=main_rus1)


@dp.message(F.text == "Karzina🛒")
async def start_function(message: types.Message):
    await message.answer("Siz Karxina bolimidasiz bu joyda siz karzinani sotib olishingiz mumkin!", reply_markup=main_button5)



@dp.message(F.text == "Biz haqimizda📁")
async def start_function(message: types.Message):
    await message.answer("Bu bizning haqimizda", reply_markup=button7)


@dp.callback_query(F.data == "sayt")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("BU bizning sayt!", reply_markup=main_button2)

@dp.message(F.text == "Kurs📕")
async def start_function(message: types.Message):
    await message.answer("Bu Kurs bomilimi bu joyda siz ozin"
                         "gizga kerak bolgan kursni sotib ols"
                         "angiz boladi!", reply_markup=main_button4)

@dp.message(F.text == "Back-end📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd"
                                     "9GcS7IY4h7aKuG61G76syRqYEIn3Di99B5OeKQw&s",
                               caption=" Backend (inglizcha back-end) - bu xizmatning dasturiy ta'minot va apparat qismidir. Bu veb-sayt mantig'i amalga oshiriladigan vositalar to'plami. Bu bizning ko'zimizdan yashiringan narsa, ya'ni kompyuter va brauzerdan tashqarida sodir bo'ladi. (Back End) Orqa tomon ishlab chiquvchilari veb-saytlarning foydalanuvchilar bilan bevosi"
                                       "ta aloqasi bo'lmagan qopqoq ostida qismlari"
                                       "ni yaratadilar.    Backend (back end, back-"
                                       "end) esa Frontendning aksi hisoblanib, qaysid"
                                       "ir narsaning ichki, yoki orqa tomoni degan ma"
                                       "noni anglatadi. Bu bilan biz qaysidir narsani"
                                       "ng hammaga korinmaydigan, yashirin, ichki yoki"
                                       " orqa tomonini nazarda tutgan bolamiz. Narxi:1mln"
                                       " so'm(oyiga)! ", reply_markup=button1)

@dp.message(F.text == "Front-end📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://as1.ftcdn.net/v2/jpg/02/58/05/02"
                                     " /1000_F_258050259_lMQwrjDHXMT7tmkgVS9nAtrNRJmB57fh.jpg",
                               caption="Front-End haqida yozishdan oldin sizga "
                                       "kichik bir narsa haqida ma’lumot berib o’tmoqchiman. Veb sahifani kodlashtirish asosiy ikki qismga bo’linadi. Front-End va Back-End. Back-End dasturlovchi veb-saytning bazasi, serveri va shunga o’xshash ishlari bilan shug’ullanandi. Back-End so’zning ma’nosidan ham ma’lumki bu yo’nalishdagi dasturchi asosan foydalanuvchiga ko’rinmaydiga ishlar bilan shug’ullanadi. Back-End ha"
                                       "qida ko’proq keyingi maqolalarda o’qish"
                                       "ingiz mumkin, hozir esa Front-End haqida"
                                       ".Front-End dasturlovchi veb-saytning foyd"
                                       "alanuvchiga korinadigan qismini tayyorlas"
                                       "h bilan shugullanadi. Masalan siz veb-sayt"
                                       "larda koradigan oddiygina tugma uchun ham "
                                       "Front-End dasturlovchi mehnat qilib kod yoz"
                                       "adi. Yani siz brauzer orqali ekranda korib t"
                                       "uradigan barcha narsani tayyorlash Front-End"
                                       " dasturchining vazifasi va mana shu tayyorla"
                                       "ngan ishlarning jamlanmasi veb-saytning Fron"
                                       "t-End qismi deyiladi. Yanada soddaroq tushun"
                                       "tiradigan bolsam siz veb-sayt nomini brauzerg"
                                       "a yozib, veb-saytga kirganingizda sizga korini"
                                       "xb turgan qismi Front-End qismi hisoblanadi. "
                                       "Narxi:500.000(oyiga)so'm", reply_markup=button2)

@dp.message(F.text == "Starter📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q="
                                     "tbn:ANd9GcTWETiL2uhPUerUVVGU4tUlpKN8ADx8HqU2nw&s",
                               caption="Starter bu kursda siz Starterni org"
                                       "anasiz :))) Narxi:100.000(oyiga) so'm", reply_markup=button3)

@dp.message(F.text == "Pro📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuUaNLuwTR26WEcdANG95bU272fBIj9heuNA&s",
                               caption="Siz bu kursda starterdan koproq nars"
                                       "alarni organasiz :)) narxi:200.000(oyiga) so'm", reply_markup=button4)

@dp.message(F.text == "Design📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaqs7fQ6UtAkWsDbpD-WVwE0wWKmd1PovXuA&s",
                               caption="Dizayn (inglizcha: design — „loyiha“, „chizma“, „rasm“) "
                                       "— narsalar muhitini estetik va funksional sifatlarini shak"
                                       "llantirish maqsadiga qaratilgan loyihalash faoliyati turlar"
                                       "ini ifodalovchi termin. Dizayn faoliyati tarkibiga keng ist"
                                       "eʼmol buyumlari, mashina, dastgoh, kiyim, reklama va oʻrov m"
                                       "ateriallari, i. ch., jamoat va turar joy binolarini jihozlas"
                                       "h, mebel va b. kiradi. Dizayn 20-asr boshlarida yuzaga kelib,"
                                       " 1930-yillarda maxsus faoliyat turi sifatida Gʻarbiy Yevropa "
                                       "va AQShda shakllandi. 1980-yil 2-yarmidan dizaynning faoliyat"
                                       " doirasi kengaydi. Dizaynerlar rassom sezgisi bilan birga ilmi"
                                       "y fanlar (masalan, materialshunoslik, rangshunoslik va boshqa"
                                       ")ga tayanadi, i. ch. jarayoni va sharoitlari, sotsiologiya va "
                                       "boshqa bilimlarga ega bulishi lozim. Dizayn sohasidagi mutaxas"
                                       "sislar maxsus oliy oʻquv yurtlaridatayyorlanadi. Jumladan, Kam"
                                       "oliddin Behzod nomidagi Milliy rassomlik va dizayn institutida ham interyerla"
                                       "r va sanoat grafikasi, libos dizayn boʻyicha mutaxassislar t"
                                       "ayyorlanadi. Narxi:700.000(oyiga) so'm", reply_markup=button5)

@dp.message(F.text == "Edit Video📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxlpfVPz9mOzq8t4Kavdg4KEYCp7FDOkoh4w&s",
                               caption="Siz bu kursda videolar"
                                       "ni yaxshi edit qilishni org"
                                       "anasiz videoga bogliq narsalrni o"
                                       "rganasiz! Narxi:400.000(oyiga) so'm", reply_markup=button6)

@dp.callback_query(F.data == "1")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button2)
    Karzina.append("Back-end")

@dp.callback_query(F.data == "2")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button2)
    Karzina.append("Front-end")

@dp.callback_query(F.data == "3")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button2)
    Karzina.append("Starter")

@dp.callback_query(F.data == "4")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button2)
    Karzina.append("Pro")

@dp.callback_query(F.data == "5")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button2)
    Karzina.append("Design")

@dp.callback_query(F.data == "6")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button2)
    Karzina.append("Video Edit")

@dp.message(F.text == "Humo💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz Uzcard kartangizni nomerini jonating")


@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'r", reply_markup=main_button2)
    Karzina.clear()
    await state.clear()

@dp.message(F.text == "UzCard💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz Uzcard kartangizni nomerini jonating")


@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'r", reply_markup=main_button2)
    Karzina.clear()
    await state.clear()

async def reg_one():
    pass

@dp.message(F.text == "Karzina")
async def start(message: types.Message):
    await message.answer(f"{Karzina}")

@dp.callback_query(F.data == "olmaslik")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz tovarni sotib olmadingiz", reply_markup=main_button2)

@dp.message(F.text == "Sotib Olish")
async def start_function(message: types.Message):
    await message.answer("Siz tovarni sotib oldingiz!", reply_markup=main_button2)

@dp.message(F.text == "Sotib olmaslik")
async def start_function(message: types.Message):
    await message.answer("Siz tovarni sotib olmadingiz", reply_markup=main_button2)

@dp.message(F.text == "olmaslik2")
async def start_function(message: types.Message):
    await message.answer("Sz ytga yuborildingiz!", reply_markup=main_button2)
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################


@dp.message(F.text == "Карзина🛒")
async def start_function(message: types.Message):
    await message.answer("Siz Karxina bolimidasiz bu joyda siz karzinani sotib"
                         " olishingiz mumkin!", reply_markup=main_rus3)



@dp.message(F.text == "о нас📁")
async def start_function(message: types.Message):
    await message.answer("Bu bizning haqimizda", reply_markup=button7)


@dp.callback_query(F.data == "Cайт")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("BU bizning sayt!", reply_markup=main_button2)

@dp.message(F.text == "Курс📕")
async def start_function(message: types.Message):
    await message.answer("Bu Kurs bomilimi bu joyda siz ozin"
                         "gizga kerak bolgan kursni sotib ols"
                         "angiz boladi!", reply_markup=main_rus2)

@dp.message(F.text == "Back-enD📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd"
                                     "9GcS7IY4h7aKuG61G76syRqYEIn3Di99B5OeKQw&s",
                               caption=" Backend (inglizcha back-end) - bu xizmatning dasturiy ta'minot va apparat qismidir. Bu veb-sayt mantig'i amalga oshiriladigan vositalar to'plami. Bu bizning ko'zimizdan yashiringan narsa, ya'ni kompyuter va brauzerdan tashqarida sodir bo'ladi. (Back End) Orqa tomon ishlab chiquvchilari veb-saytlarning foydalanuvchilar bilan bevosi"
                                       "ta aloqasi bo'lmagan qopqoq ostida qismlari"
                                       "ni yaratadilar.    Backend (back end, back-"
                                       "end) esa Frontendning aksi hisoblanib, qaysid"
                                       "ir narsaning ichki, yoki orqa tomoni degan ma"
                                       "noni anglatadi. Bu bilan biz qaysidir narsani"
                                       "ng hammaga korinmaydigan, yashirin, ichki yoki"
                                       " orqa tomonini nazarda tutgan bolamiz. Narxi:1mln"
                                       " so'm(oyiga)! ", reply_markup=main_rusbutton1)

@dp.message(F.text == "Front-enD📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://as1.ftcdn.net/v2/jpg/02/58/05/02"
                                     " /1000_F_258050259_lMQwrjDHXMT7tmkgVS9nAtrNRJmB57fh.jpg",
                               caption="Front-End haqida yozishdan oldin sizga "
                                       "kichik bir narsa haqida ma’lumot berib o’tmoqchiman. Veb sahifani kodlashtirish asosiy ikki qismga bo’linadi. Front-End va Back-End. Back-End dasturlovchi veb-saytning bazasi, serveri va shunga o’xshash ishlari bilan shug’ullanandi. Back-End so’zning ma’nosidan ham ma’lumki bu yo’nalishdagi dasturchi asosan foydalanuvchiga ko’rinmaydiga ishlar bilan shug’ullanadi. Back-End ha"
                                       "qida ko’proq keyingi maqolalarda o’qish"
                                       "ingiz mumkin, hozir esa Front-End haqida"
                                       ".Front-End dasturlovchi veb-saytning foyd"
                                       "alanuvchiga korinadigan qismini tayyorlas"
                                       "h bilan shugullanadi. Masalan siz veb-sayt"
                                       "larda koradigan oddiygina tugma uchun ham "
                                       "Front-End dasturlovchi mehnat qilib kod yoz"
                                       "adi. Yani siz brauzer orqali ekranda korib t"
                                       "uradigan barcha narsani tayyorlash Front-End"
                                       " dasturchining vazifasi va mana shu tayyorla"
                                       "ngan ishlarning jamlanmasi veb-saytning Fron"
                                       "t-End qismi deyiladi. Yanada soddaroq tushun"
                                       "tiradigan bolsam siz veb-sayt nomini brauzerg"
                                       "a yozib, veb-saytga kirganingizda sizga korini"
                                       "xb turgan qismi Front-End qismi hisoblanadi. "
                                       "Narxi:500.000(oyiga)so'm", reply_markup=main_rusbutton2)

@dp.message(F.text == "StarteR📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q="
                                     "tbn:ANd9GcTWETiL2uhPUerUVVGU4tUlpKN8ADx8HqU2nw&s",
                               caption="Starter bu kursda siz Starterni org"
                                       "anasiz :))) Narxi:100.000(oyiga) so'm", reply_markup=main_rusbutton3)

@dp.message(F.text == "PrO📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuUaNLuwTR26WEcdANG95bU272fBIj9heuNA&s",
                               caption="Siz bu kursda starterdan koproq nars"
                                       "alarni organasiz :)) narxi:200.0"
                                       "00(oyiga) so'm", reply_markup=main_rusbutton4)

@dp.message(F.text == "Design📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaqs7fQ6UtAkWsDbpD-WVwE0wWKmd1PovXuA&s",
                               caption="Dizayn (inglizcha: design — „loyiha“, „chizma“, „rasm“) "
                                       "— narsalar muhitini estetik va funksional sifatlarini shak"
                                       "llantirish maqsadiga qaratilgan loyihalash faoliyati turlar"
                                       "ini ifodalovchi termin. Dizayn faoliyati tarkibiga keng ist"
                                       "eʼmol buyumlari, mashina, dastgoh, kiyim, reklama va oʻrov m"
                                       "ateriallari, i. ch., jamoat va turar joy binolarini jihozlas"
                                       "h, mebel va b. kiradi. Dizayn 20-asr boshlarida yuzaga kelib,"
                                       " 1930-yillarda maxsus faoliyat turi sifatida Gʻarbiy Yevropa "
                                       "va AQShda shakllandi. 1980-yil 2-yarmidan dizaynning faoliyat"
                                       " doirasi kengaydi. Dizaynerlar rassom sezgisi bilan birga ilmi"
                                       "y fanlar (masalan, materialshunoslik, rangshunoslik va boshqa"
                                       ")ga tayanadi, i. ch. jarayoni va sharoitlari, sotsiologiya va "
                                       "boshqa bilimlarga ega bulishi lozim. Dizayn sohasidagi mutaxas"
                                       "sislar maxsus oliy oʻquv yurtlaridatayyorlanadi. Jumladan, Kam"
                                       "oliddin Behzod nomidagi Milliy rassomlik va dizayn institutida ham interyerla"
                                       "r va sanoat grafikasi, libos dizayn boʻyicha mutaxassislar t"
                                       "ayyorlanadi. Narxi:700.000(oyiga) so'm", reply_markup=main_rusbutton5)

@dp.message(F.text == "Edit Video📕")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxlpfVPz9mOzq8t4Kavdg4KEYCp7FDOkoh4w&s",
                               caption="Siz bu kursda videolar"
                                       "ni yaxshi edit qilishni org"
                                       "anasiz videoga bogliq narsalrni o"
                                       "rganasiz! Narxi:400.000(oyiga) so'm", reply_markup=main_rusbutton6)

@dp.callback_query(F.data == "rus1b")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_rus1)
    Karzina.append("Back-end")

@dp.callback_query(F.data == "rus2b")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_rus1)
    Karzina.append("Front-end")

@dp.callback_query(F.data == "rus3b")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_rus1)
    Karzina.append("Starter")

@dp.callback_query(F.data == "rus4b")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_rus1)
    Karzina.append("Pro")

@dp.callback_query(F.data == "rus5b")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_rus1)
    Karzina.append("Design")

@dp.callback_query(F.data == "rus6b")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_rus1)
    Karzina.append("Video Edit")

@dp.message(F.text == "HumO💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz Uzcard kartangizni nomerini jonating")


@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'rt", reply_markup=main_rus1)
    Karzina.clear()
    await state.clear()

@dp.message(F.text == "UzCarD💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz Uzcard kartangizni nomerini jonating")

@dp.message(F.text == "Til ozgartirish🏴")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz til ozgartirdingiz!", reply_markup=main_button3)

@dp.message(F.text == "изменит языка🏴")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz til ozgartirdingiz!", reply_markup=main_button3)

@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'rt", reply_markup=main_rus1)
    Karzina.clear()
    await state.clear()

@dp.callback_query(F.data == "olmaslik1")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz tovarni sotib olmadingiz", reply_markup=main_rus1)

@dp.message(F.text == "купить")
async def start_function(message: types.Message):
    await message.answer("Siz tovarni sotib oldingiz!", reply_markup=main_rus2)

@dp.message(F.text == "не купить")
async def start_function(message: types.Message):
    await message.answer("Siz tovarni sotib olmadingiz", reply_markup=main_rus1)











async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())