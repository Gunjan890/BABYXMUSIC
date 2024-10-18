import random
import time
import requests
from SONALI import app
from config import BOT_USERNAME

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["gpt", "bard", "llama", "mistral", "palm", "gemini"]))
async def chatbots( Message):
    prompt = getText(m)
    media = getMedia(m)
    if media is not None:
        return await askAboutImage(_, m, [media], prompt)
    if prompt is None:
        return await m.reply_text("Hello, How can I assist you today?")
    model = m.command[0].lower()
    output = await ChatCompletion(prompt, model)
    if model == "bard":
        output, images = output
        if len(images) == 0:
            return await m.reply_text(output)
        media = []
        for i in images:
            media.append(t.InputMediaPhoto(i))
        media[0] = t.InputMediaPhoto(images[0], caption=output)
        await _.send_media_group(
            m.chat.id,
            media,
            reply_to_message_id=m.id
        )
        return
    await m.reply_text(output['parts'][0]['text'] if model == "gemini" else output)

async def askAboutImage( Message, mediaFiles: list, prompt: str):
    images = []
    for media in mediaFiles:
        image = await _.download_media(media.file_id, file_name=f'./downloads/{m.from_user.id}_ask.jpg')
        images.append(image)
    output = await geminiVision(prompt if prompt else "What's this?", "geminiVision", images)
    await m.reply_text(output)
    
