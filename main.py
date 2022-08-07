# -*- coding: utf-8 -*-
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageEmpty

from time import sleep
import codecs
import re
from threading import Timer

from config import *

app = Client('my_account', api_id=API_ID, api_hash=API_HASH)
print('Loaded')


REPLACEMENT_MAP = {'А': 'ɐ', 'Б': 'ƍ', 'В': 'ʚ', 'Г': 'ɹ', 'Д': 'ɓ', 'Е': 'ǝ', 'Ё': 'ǝ', 'Ж': 'ж', 'З': 'ε', 'И': 'и',
                   'Й': 'ņ', 'К': 'ʞ', 'Л': 'v', 'М': 'w', 'Н': 'н', 'О': 'о', 'П': 'u', 'Р': 'd', 'С': 'ɔ', 'Т': 'ɯ',
                   'У': 'ʎ', 'Ф': 'ф', 'Х': 'х', 'Ц': 'ǹ', 'Ч': 'Һ', 'Ш': 'm', 'Щ': 'm', 'Ъ': 'q', 'Ь': 'q', 'Э': 'є',
                   'Я': 'ʁ', 'а': 'ɐ', 'б': 'ƍ', 'в': 'ʚ', 'г': 'ɹ', 'д': 'ɓ', 'е': 'ǝ', 'ё': 'ǝ', 'ж': 'ж', 'з': 'ε',
                   'и': 'и', 'й': 'ņ', 'к': 'ʞ', 'л': 'v', 'м': 'w', 'н': 'н', 'о': 'о', 'п': 'u', 'р': 'd', 'с': 'ɔ',
                   'т': 'ɯ', 'у': 'ʎ', 'ф': 'ф', 'х': 'х', 'ц': 'ǹ', 'ч': 'Һ', 'ш': 'm', 'щ': 'm', 'ъ': 'q', 'ь': 'q',
                   'э': 'є', 'я': 'ʁ', 'A': 'ɐ', 'B': 'q', 'C': 'ɔ', 'D': 'р', 'E': 'ǝ', 'F': 'ɟ', 'G': 'ƃ', 'H': 'ɥ',
                   'I': 'ı', 'J': 'ɾ', 'K': 'ʞ', 'L': 'l', 'M': 'щ', 'N': 'u', 'O': 'o', 'P': 'd', 'Q': 'ь', 'R': 'ɹ',
                   'S': 's', 'T': 'ʇ', 'U': 'п', 'V': 'л', 'W': 'м', 'X': 'x', 'Y': 'ʎ', 'Z': 'z', 'a': 'ɐ', 'b': 'q',
                   'c': 'ɔ', 'd': 'р', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ı', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l',
                   'm': 'щ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'ь', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'п', 'v': 'л',
                   'w': 'м', 'x': 'x', 'y': 'ʎ', 'z': 'z'}
@app.on_message(filters.command('flip', prefixes='.') & filters.me)
def flip(_, msg):
    """
    This function is used to flip message with replacement map.
    """
    global REPLACEMENT_MAP
    formatted_message = msg.text.split('.flip', maxsplit=1)[1].strip()
    final_message = ''
    for c in formatted_message:
        if c in REPLACEMENT_MAP:
            final_message += REPLACEMENT_MAP[c]
        else:
            final_message += c
    msg.edit(final_message[::-1])


@app.on_message(filters.command('print', prefixes='.') & filters.me)
def beautiful_type(_, msg):
    """
    This function is used to print out the message in a beautiful way.
    """
    formatted_message = msg.text.split('.print', maxsplit=1)[1].strip()
    for i in range(1, len(formatted_message)):
        try:
            msg.edit(formatted_message[:i]+'▒')
            sleep(0.05)
        except FloodWait as e:
            sleep(e.value)
        except MessageEmpty:
            pass
        try:
            msg.edit(formatted_message[:i+1])
            sleep(0.05)
        except FloodWait as e:
            sleep(e.value)
        except MessageEmpty:
            pass


@app.on_message(filters.command('bio', prefixes='.') & filters.me)
def bio(_, msg):
    """
    This function is used to set and change bio.
    If no argument is given, it will return the current bio.
    If an argument is given, it will set the bio to the given argument.
    Bio is saved in the bio.txt file.
    """
    formatted_message = msg.text.split('.bio', maxsplit=1)[1].strip()
    if formatted_message == '':
        with codecs.open('bio.txt', 'r', 'utf-8') as f:
            msg.edit(f.read())
    else:
        with codecs.open('bio.txt', 'w', 'utf-8') as f:
            f.write(formatted_message)
            msg.edit('Bio set to:\n' + formatted_message)


@app.on_message(filters.command('eval', prefixes='.') & filters.me)
def eval_msg(_, msg):
    """
    Evaluates the given expression.
    """
    formatted_message = msg.text.split('.eval', maxsplit=1)[1].strip()
    msg.edit(f'{eval(formatted_message):.4f}')


@app.on_message(filters.command('all', prefixes=['.', '@']) & filters.me)
def mention_all(_, msg):
    """
    This function is used to mention all users in the chat.
    """
    s = ''
    members = msg.chat.get_members()
    try:
        for user in members:
            if user.user.username is not None:
                s += '@' + user.user.username + ' '
            else:
                s += str(user.user.mention()) + ' '
    except Exception as e:
        msg.edit('Can\'t get members.')
        return
    s = s[:-1]
    msg.delete()
    app.send_message(msg.chat.id, s)


@app.on_message(filters.command('all_names', prefixes=['.', '@']) & filters.me)
def text_mention_all(_, msg):
    """
    This function is used to mention all users with their names in the chat.
    """
    s = ''
    members = msg.chat.get_members()
    try:
        for user in members:
            s += str(user.user.mention()) + ' '
    except Exception as e:
        msg.edit('Can\'t get members.')
        return
    s = s[:-1]
    msg.delete()
    app.send_message(msg.chat.id, s)


async def ping_filter(_, __, query):
    """
    Filter for mention_with_text function.
    """
    return re.fullmatch(r'@[a-zA-Z0-9_]{5,}\[.+\]', query.text)

static_ping_filter = filters.create(ping_filter)


@app.on_message(static_ping_filter & filters.me)
def mention_with_text(_, msg):
    """
    Mentions a user which has nickname with text.
    Format: @username[text]
    """
    nickname, text = msg.text[1:-1].split('[')
    msg.edit('yep')
    msg.delete()
    app.send_message(msg.chat.id, f'[{text}](http://t.me/{nickname})', disable_web_page_preview=True)


@app.on_message(filters.command('remind', prefixes='.') & filters.me)
def create_remind(_, msg):
    """
    Send you a reminder in this chat.
    Format: .remind time text
    Time format: number+s/m/h/d
    """
    _, time_interval, content = msg.text.split(' ', maxsplit=2)
    if time_interval[-1] == 's':
        time_interval = int(time_interval[:-1])
    elif time_interval[-1] == 'm':
        time_interval = int(time_interval[:-1]) * 60
    elif time_interval[-1] == 'h':
        time_interval = int(time_interval[:-1]) * 60 * 60
    elif time_interval[-1] == 'd':
        time_interval = int(time_interval[:-1]) * 60 * 60 * 24

    msg.edit('Reminder set.')

    # run send reminder function in the future
    t = Timer(time_interval, app.send_message, args=(msg.chat.id, content))
    t.start()


@app.on_message(filters.command('repo', prefixes='.') & filters.me)
def send_repo(_, msg):
    """
    Send url to the repo.
    """
    msg.edit('https://github.com/IronGunYT/userBotTg')


app.run()
