import asyncio
import json
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# ضع توكن بوتك هنا بين علامتي التنصيص
TOKEN = "8672620524:AAFSiLlvDghCXSgApNE73cLOmSYM8aWdncY"
# ضع معرف قناتك هنا (مثال: @SheinDealsSA_Channel)
CHANNEL_ID = "@اسم_قناتك_هنا"

async def main():
    bot = Bot(token=TOKEN)
    
    if not os.path.exists("offers.json"):
        print("ملف offers.json غير موجود!")
        return

    with open("offers.json", "r", encoding="utf-8") as f:
        offers = json.load(f)

    if not offers:
        print("لا توجد عروض متبقية في القائمة!")
        return

    # أخذ أول عرض في الدور
    offer = offers[0]
    
    # تنسيق رسالة العرض
    caption = (
        f"🛍️ **{offer['title']}**\n\n"
        f"💰 السعر: {offer['price']}\n"
        f"🔥 الخصم: {offer['discount']}\n\n"
        f"👇 اضغط للطلب برابط العمولة:"
    )

    # زر الشراء برابط الشركاء الخاص بك
    keyboard = [[InlineKeyboardButton("🛒 اشتري الآن", url=offer['affiliate_url'])]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # إرسال العرض للقناة
    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=offer['image_url'],
        caption=caption,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

    print("تم نشر العرض بنجاح!")

    # حذف العرض المنشور من القائمة حتى لا يتكرر في المرة القادمة
    offers.pop(0)
    with open("offers.json", "w", encoding="utf-8") as f:
        json.dump(offers, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
