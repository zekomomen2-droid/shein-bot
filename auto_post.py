import json
import random
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8672620524:AAHwMHQcrAKBx3mBhd05Z_l_kFmp5D9ip08"
CHANNEL = "@SheinDealsSA_Channel"

async def main():
    bot = Bot(token=TOKEN)
    
    try:
        with open("offers.json", "r", encoding="utf-8") as f:
            offers = json.load(f)
    except Exception as e:
        print(f"Error reading offers.json: {e}")
        return
    
    if not offers:
        print("offers.json is empty!")
        return

    offer = random.choice(offers)
    
    keyboard = [
        [
            InlineKeyboardButton("🛒 اشترِ الآن", url=offer.get("url", "https://t.me"))
        ]
    ]
    
    caption = f"🛍️ {offer.get('title', '')}\n\n💰 السعر: {offer.get('price', '')}\n🔥 الخصم: {offer.get('discount', '')}"
    
    await bot.send_photo(
        chat_id=CHANNEL,
        photo=offer.get("image"),
        caption=caption,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    print("✅ تم نشر العرض تلقائياً بنجاح!")

if __name__ == "__main__":
    asyncio.run(main())
