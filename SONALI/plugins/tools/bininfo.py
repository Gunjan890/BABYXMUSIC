from SONALI import *
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import *
from SONALI import pbot as app 

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "⬤ <b>ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀ ʙɪɴ ᴛᴏ ɢᴇᴛ ʙɪɴ ᴅᴇᴛᴀɪʟs !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("⚡")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("❌")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b>❖ ʙɪɴ ғᴜʟʟ ᴅᴇᴛᴀɪʟs ❖</b>

<b>● ʙᴀɴᴋ ➥</b> <tt>{resp.bank}</tt>
<b>● ʙɪɴ ➥</b> <tt>{resp.bin}</tt>
<b>● ᴄᴏᴜɴᴛʀʏ ➥</b> <tt>{resp.country}</tt>
<b>● ғʟᴀɢ ➥</b> <tt>{resp.flag}</tt>
<b>● ɪsᴏ ➥</b> <tt>{resp.iso}</tt>
<b>● ʟᴇᴠᴇʟ ➥</b> <tt>{resp.level}</tt>
<b>● ᴘʀᴇᴘᴀɪᴅ ➥</b> <tt>{resp.prepaid}</tt>
<b>● ᴛʏᴘᴇ ➥</b> <tt>{resp.type}</tt>
<b>● ᴠᴇɴᴅᴏʀ ➥</b> <tt>{resp.vendor}</tt>""", reply_markup=InlineKeyboardMarkup(EVAA),
        )
    except:
        return await aux.edit(f"""
⬤ ʙɪɴ ɴᴏᴛ ʀᴇᴄᴏɢɴɪᴢᴇᴅ, ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ʙɪɴ.""")


__help__ = """

⬤ /gen ➥ ɢᴇɴʀᴀᴛᴇ ᴄʀᴇᴅɪᴛ ᴄᴀʀᴅs [● ᴇx ➣ /ɢᴇɴᴄᴄ 123456]
⬤ /bininfo ➥ ʙɪɴ ᴅᴇᴛᴀɪʟs [● ᴇx ➣ /ʙɪɴɪɴғᴏ 123456]
⬤ /fake ➥ ғᴀᴋᴇ ɪɴғᴏ ғᴏʀ ʙɪɴ [● ᴇx ➣ /ғᴀᴋᴇ ᴜs] 
⬤ /genbin ➥ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ʀᴀɴᴅᴏᴍ ᴠᴀʟɪᴅ ʙɪɴ.
⬤ /rand ➥ ʙɪɴ ᴅᴀᴛᴀ.
⬤ /fakegen ➥ ᴜsᴇʀ ғᴀᴋᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
"""

__mod_name__ = "ᴄᴄ ʙɪɴ"
