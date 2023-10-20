from pyrogram import Client
from pyrogram.types import Message

from baidufanyi_test import BaiDuFanYi

api_id = "27175683"
api_hash = "ff5bd7a1d985ad6e6db389e4ef104fe6"
bot_token = "6778102881:AAEJ0PvBN8qDjR3MqNSGNFWUXaLacuKbQ7Y"

app = Client(
    "kjjjkljklbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@app.on_message()
async def echo(client: Client, message: Message):
    print("开始查询：" + message.text)
    res_text = BaiDuFanYi().getfanyi(message.text)
    # await message.reply(message.text)
    await message.reply(res_text)


app.run()
