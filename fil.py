import random
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from new import *
from config import *
from threading import Thread
import datetime

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "3":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "4":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "5":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "7":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "9":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "10":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "11":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "12":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    return username

@turbo.on(events.NewMessage(outgoing=True, pattern=r"تشيكر"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
    
@turbo.on(events.NewMessage(outgoing=True, pattern=r"الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
    else:
        
@turbo.on(events.NewMessage(outgoing=True, pattern=r"صيد"))
async def _(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[1])
        choice = str(msg[0])
        trys = 0
        await event.edit(f"**Ok I will check  `{choice}` from the user  `{ch}`**")

        @turbo.on(events.NewMessage(outgoing=True, pattern=r"الصيد"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"The examination has arrived **({trys})** of attempts")
                elif "off" in isclaim:
                    await event.edit("There is NO working check !")
                else:
                    await event.edit("mistake")
            else:
                pass
        for i in range(818181):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await turbo(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await turbo.send_file(event.chat_id, 'https://t.me/jc_ksa/17', caption=f'''Leader : @AbnBashar
User ⤷ @{username}
Save ⤷ ch
Clicks ⤷ {trys}
turbo ⤷ @turboBH
''')
                    await turbo.send_file("i5tbot", 'https://t.me/jc_ksa/17', caption=f'''Leader : @AbnBashar
User ⤷ @{username}
Save ⤷ Flod - turbo
Clicks ⤷ {trys}
turbo ⤷ @turboBH
''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    msg = await turbo.send_message(event.chat_id, f'''error with {username}
                    {str(eee)}''')
                    if "The username is already taken (caused by UpdateUsernameRequest)" in msg: 
                        N = datetime.datetime.now()
                        await event.edit(f"{username} خاصيه \n الوقت هو {N}") 
                    if "A wait of" in str(eee):
                        break
                    else:
                        await turbo.send_message(event.chat.id, "")
            else:
                pass
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await event.client.send_message(event.chat_id, "")
    else:
        await event.edit("")
        
@turbo.on(events.NewMessage(outgoing=True, pattern=r"تثبيت"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "قناة":
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[1])
            ch = str(msg[0])
            await turbo.send_message(event.chat_id, f"Started successfully → `{ch}`")
            for i in range(15000000):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await turbo(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        trys += 12
                        await turbo.send_file(event.chat_id, 'https://t.me/jc_ksa/17', caption=f'''Leader : @AbnBashar
User ⤷ @{username}
Save ⤷ Channel
Clicks ⤷ {trys}
turbo ⤷ @turboBH''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"band the @{username} ")
                    except Exception as eee:
                    	await turbo.send_message(event.chat_id, f'''{username}
- {str(eee)} -''')
                    if "A wait of" in str(eee):
                        break
                else: 
                    pass
                trys += 1

            trys = ""
            isauto.clear()
            isauto.append("off")
            await turbo.send_message(event.chat_id, "done ⤷ 1")
