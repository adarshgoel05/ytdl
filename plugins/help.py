from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url   ⭕{message.from_user.first_name}⭕always choose the best quality for better result(Under 2GB)"
    await message.reply_text(helptxt)
