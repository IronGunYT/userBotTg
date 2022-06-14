<h1 align="center">userBotTg</h1>
<br>

A Telegram user bot for Python with multiple features.

## Commands

### Flip

Flips message upside down

syntax: `.flip text`

example: `.flip hello`

### Print

Beutiful typing of text

syntax: `.print text`

example: `.print Lorem Ipsum`

### Edit Bio

Changes Bio

syntax: `.bio text`

example: `.bio Hello there!`

### Send Bio

Sends Bio

syntax: `.bio`

example: `.bio`

### Eval

Evaluates the given expression

syntax: `.eval expression`

example: `.eval 2+2*2-2**.5`

### Mention all

Mentions all users in current chat

syntax: `@all`, `.all`

example: `@all`

### Text mention all

Mentions all users in current chat with their names

syntax: `@all_names`, `.all_names`

example: `@all_names`

### Beautiful mention

Mentions user in current chat with string

syntax: `@username[text]`

example: `@IronGun[python developer]`

### Repo url

Sends url to this repo

syntax: `.repo`

example: `.repo`

### Reminds

Send you a reminder in this chat through given time

syntax: `.remind time text`

time syntax: number and s/m/h/d:
- s - seconds
- m - minutes
- h - hours
- d - days

example: `.remind 30m Close window`

## Installation

 1. Clone the repository
 2. Install all the requirements using cmd
 `pip3 install -r requirements.txt`
 3. Rename `template_config.py` to `config.py`
 4. Fill in api id and hash in config. You can get them [here](https://my.telegram.org/apps)
 5. Run the UserBot using systemctl([Russian guide](https://help.sprintbox.ru/perl-python-nodejs/python-telegram-bots#bot-launch))
 6. Paste your phone and verify it
