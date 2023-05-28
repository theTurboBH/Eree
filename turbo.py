from telethon.tl.functions.channels import JoinChannelRequest
from telethon import events
from new import *
from config import *
from fil import *


turbo.start()


@turbo.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@turbo.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    await turbo(JoinChannelRequest("ALIBAASHAR"))
    await event.edit(f'''turbo bh W.r.k ✅
''')

@turbo.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف الصيد"))
async def update(event):
    await event.edit("جارِ ايقاف الصيد  ✿\n انتضࢪ 2 دقيقه Π \n @Turbobh - @AbnBashar")
    await turbo.disconnect()
    await turbo.send_message("me", "`تم ايقاف الصيد !`")


turbo.run_until_disconnected()