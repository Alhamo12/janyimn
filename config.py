## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBRSx_VKahK04OyrkVT1JeC3LDVOHuqTV8_2a9SaS0LYQx7ZBkglOdmQl2L38OWvzXwSj1Tb13dltXlE4Esy4jk1-ahz4MK-7UMBDgQZLVAw9IDLG4gLuEv7PDTeYvhD3mTe2bNxzb7WndHksCA1qhkNDysOfyrrWhaNq3MG8NhOfzmp5rw_nW4B31cV07MgpeP1sBFJC8mGSIR12ZdjKSuyS3ns3zLLZLjX4YSjFU-g9Z6ro_GbIkVSd259nisK7RYw5XIC7cXxFu82XXxxXmq-KNi5XfTAcuf2a0bST--bqwM0omN39eKRFIZoc7YcMa24exvs-twsfRRE-ADzEIxAAAAATqRNTEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5401619253:AAG_eL0rFDMDS1XL9m3OBafwDRy6pPAG_CQ")
BOT_NAME = getenv("BOT_NAME", "jan")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "jano")
OWNER_USERNAME = getenv("OWNER_USERNAME", "J_A_N_U_O_1")
ALIVE_NAME = getenv("ALIVE_NAME", "jano")
BOT_USERNAME = getenv("BOT_USERNAME", "llllll_M_llllll_bot")
OWNER_ID = getenv("OWNER_ID", "5277562161")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ljl_a_lnl")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "akd444s")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "akd444s")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5277562161").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
