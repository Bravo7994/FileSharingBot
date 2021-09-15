#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>◉ Creator : <a href='tg://user?id=1059785066'>𝗣𝗟𝗔𝐘 𝗕𝗢𝐘</a>\n◉ Language : <code>Python3</code>\n◉ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n◉ Channel : @Movies_Emperio\n◉ Support Group : @Cinemas_Empire</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 BACK", callback_data = "start"),
                        InlineKeyboardButton("🔒 CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "back":
        uso = str(query.from_user.first_name)
        text = f"<b>Hello {uso},</b>\n\nI Can Store 𝐌𝐎𝐕𝐈𝐄𝐒 𝐄𝐌𝐏𝐎𝐑𝐈𝐎 Files In This Bot And Other Users Can Access It From Special Link 📎\n\n<b><a href='https://t.me/movies_emperio'>YOU NEED TO JOIN IN OUR CHANNEL TO DOWNLOAD THE MOVIE FILES 📂</a></b>"
        reply_markup = InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("👤 ABOUT ME", callback_data = "about"),
                                    InlineKeyboardButton("🔒 CLOSE", callback_data = "close")
                                ],
                                [
                                    InlineKeyboardButton("CLICK HERE TO JOIN THE CHANNEL", url = client.invitelink)
                                ]
                            ]
                        )

        await query.message.edit_text(
            text = text,
            reply_markup = reply_markup,
            quote = True,
            disable_web_page_preview = True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
