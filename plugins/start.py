from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Contact me", url="https://t.me/adarshgoelo5")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/adarshgoelo5")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}☺️</b>\n   use /help for More info \n      use this bot and get the video in 2-5 minutes depending on the size \n                     <B>{message.from_user.first_name}</B> the file should be under 2GB because telegram desn't support bigger files  can't help.\n  made by @adarshgoelo5"                         
    await message.reply_text(welcomed, reply_markup=joinButton) 
    raise StopPropagation
