from datetime import datetime, time, timedelta
import os
import json
import asyncio
from pickle import FALSE
import sys
import random
import types
from datetime import datetime, timedelta
import os
import json
import asyncio
import sys
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient as TMPTelegramClient
from telethon.errors import PhoneNumberFloodError, SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateUsernameRequest, UpdateProfileRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest

from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.types import Channel
import requests
from telethon import TelegramClient, events, Button
import telethon
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.sync import TelegramClient as TMPTelegramClient
from PIL import Image
import urllib.request as urllib
import io
from telethon import functions
from telethon.errors import PhoneNumberFloodError, SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateUsernameRequest, UpdateProfileRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import pickle
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import string
import os
import json
import asyncio
from logging import basicConfig, getLogger, WARNING
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient as TMPTelegramClient
from telethon.errors import PhoneNumberFloodError, SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetChatsRequest
from telethon.sessions import StringSession


def getquantity(country):
    r = requests.get(
        'https://5sim.net/v1/guest/products/' + country + '/' + "any", headers=headers)
    json = json = r.json()
    qnt = json["telegram"]["Qty"]


devices = {0: {"m_name": "Samsung Galaxy S23 Ultra", "s_name": "SDK 34", "s_app": "10.15.1"},
           1: {"m_name": "iPhone 12", "s_name": "15.1.1", "s_app": "8.3.1"},
           2: {"m_name": "iPhone 7", "s_name": "14.5.1", "s_app": "6.2.1"},
           3: {"m_name": "iPhone 5", "s_name": "14.5.1", "s_app": "6.0.1"},
           4: {"m_name": "iPhone 6", "s_name": "14.4.2", "s_app": "7.6"}}

def load_device():
    if os.path.exists("device.pk"):
        with open("device.pk", "rb") as rrrr:
            try:
                c = pickle.load(rrrr)
                if len(c) < 1:
                    return random.choice(devices)
                return c
            except Exception as e:
                print(f"Errore nel caricamento del dispositivo: {e}")
                return random.choice(devices)
    else:
        return random.choice(devices)

def save_device(device):
    with open("device.pk", "wb") as pkw:
        pickle.dump(device, pkw)
    print(f"Dispositivo salvato: {device['m_name']}")

actualdevice = load_device()


stop = True
admin = 6974360322
ADMIN = 6974360322  # TUO CHAT ID

API_KEY = 25765102
API_HASH = "ea1f34752c0860fa799b4153da5c5554"  # API HASH
toadd = []

nome = ["ᏢᎥᎬᏒᎶᎥᎾᏒᎶᎥᎾ ̪͔͈̖͗́̌́̏̅ͮᴾᴳ ²⁰⁰¹", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "🄳🅁🄰🄺🄴", "𝖆𝖈𝖕𝖎𝖓𝖌𝖚𝖎𝖓𝖔𝖊💔𝖈𝖈𝖍𝖎𝖉𝖚𝖊𝖕𝖚𝖓𝖙𝖎 🍯", "🧊Heisenberg🧊",
    "👑𝕂𝕀ℕ𝔾👑", "𝖣㋛︎𝖭'𝖳 𝗣𝗔𝗡𝗜𝗖", "☾︎✰𝙰𝚣𝙸𝚣𝙱𝚎𝙺☾︎✰", "🔥 𝐓𝐨𝐫𝐞𝐭𝐭𝐨 𝐈𝐏𝐓𝐕 | ᶠᵃˢᵗ & ᴵᴾᵀᵛ 🔥", "GetPvPᴾˡᵃᵍᵘ🇦🇱"]

cognome = ["𝕊𝕌𝕏ℝ𝕆𝔹_𝔻𝕆𝔹ℝ𝕀𝕐", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "𝔸𝕡𝕠𝕔𝕒𝕝𝕪𝕡𝕤𝕖_𝕀𝕡𝕥𝕧", "» 𝐛𝐞𝐫𝐭! ✰",
    "🆂🅷🆄🅷🆁🅰️🆃 ∅", "𝐊𝐢𝐝𝐝𝐲 🧑‍💻", "☪︎⋆ ᎡᏆᏟᏦᎽ ᏚᎻᏫᏢ ☪︎⋆", "4𝐌𝐒1𝐗 "]
    
STRING_SESSION = ""
users = []
oidocrop = True
ADMINS = []
Getter = None
Number = None
TempClient = None
five_sim_api = None
five_sim_client = None
Grab = None
activeusers = True
autoleave=False
inAdding = False
canAdd = True
maxusers = 0
AddedUsers = []
tentativi = 0
countusers = 0


smspva_client = None
Limitator = True
onlinesim_api = None
onlinesim_client = None
if os.path.exists("fivesim.txt"):
    api = open("fivesim.txt", "r")
else:
    a = open("fivesim.txt", "w")
if os.path.exists("databaseblack.db"):
    c = open("databaseblack.db", "r")
else:
    q = open("databaseblack.db", "w")

if os.path.exists("smspva.txt"):
    s = open("smspva.txt", "r")
    smspva_api = s.read()
else:
    s = open("smspva.txt", "w")
s = open("smspva.txt", "r")
smspva_api = s.read()
if not os.path.exists("country.txt"):
    open("country.txt", "w")


if os.path.exists("raspaintelligentelist.json"):
    with open("raspaintelligentelist.json", "r+") as f:
        raspingintelligentelist = json.load(f)
else:
    raspingintelligentelist = {}
    with open("raspaintelligentelist.json", "w+") as f:
        json.dump(raspingintelligentelist, f)

if os.path.exists("SSs.json"):
    with open("SSs.json", "r+") as f:
        SSs = json.load(f)
else:
    SSs = {}
    with open("SSs.json", "w+") as f:
        json.dump(SSs, f)

if os.path.exists("ArchSSs.json"):
    with open("ArchSSs.json", "r+") as f:
        ArchSSs = json.load(f)
else:
    ArchSSs = {}
    with open("ArchSSs.json", "w+") as f:
        json.dump(ArchSSs, f)

a = open("smspva.txt", "r")
smspva_api = a.read()


def saveSS():
    global SSs
    with open("SSs.json", "w+") as f:
        json.dump(SSs, f)


path = (random.choice(("immagine.jpg", 'imag.jpg')))


def getbalancesms(apikey):
    r = requests.get(
        "http://smspva.com/priemnik.php?metod=get_balance&service=opt29&apikey="+apikey)
    json = r.json()
    credito = json["balance"]
    return credito


def getbalance(api):
    headers = {
        'Authorization': 'Bearer ' + api,
        'Accept': 'application/json',
    }
    r = requests.get('https://5sim.net/v1/user/profile', headers=headers)
    json = r.json()
    balance = json["balance"]
    return balance


def saveArchSS():
    global ArchSSs
    with open("ArchSSs.json", "w+") as f:
        json.dump(ArchSSs, f)


async def joinGroups(SS, groups):
	global ADMIN, SSs, API_KEY, API_HASH
	isAlive = False
	CClient = TMPTelegramClient(StringSession(SSs[SS]), API_KEY, API_HASH)
	await CClient.connect()
	try:
		me = await CClient.get_me()
		if me == None:
			isAlive = False
		else:
			isAlive = True
	except:
		isAlive = False
	if isAlive:
		async with CClient as client:
			for group in groups:
				try:
					await client(JoinChannelRequest(group))
				except FloodWaitError as err:
					await asyncio.sleep(err.seconds + 2)
					try:
						await client(JoinChannelRequest(group))
					except:
						pass
				except:
					pass


async def removeinv():
	global API_KEY, API_HASH
	with open("SSs.json", "r+") as f:
		SSs = json.load(f)
	INVALID = []
	await bot.send_message(ADMIN, "OPERAZIONE IN CORSO.....")
	for SS in SSs:
		try:
			isAlive = False
			CClient = TMPTelegramClient(StringSession(SSs[SS]), API_KEY, API_HASH)
			await CClient.connect()
			try:
				me = await CClient.get_me()
				if me == None:
					isAlive = False
				else:
					isAlive = True
			except:
				isAlive = False
			if isAlive:
				async with CClient as client:
					try:
						await client(functions.auth.ResetAuthorizationsRequest())
					except:
						pass
			else:
				INVALID.append(SS)
		except:
			INVALID.append(SS)
	if INVALID.__len__() > 0:
		c = 0
		for SS in INVALID:
			if SS in SSs:
				del(SSs[SS])
				c += 1
		with open("SSs.json", "w+") as f:
			json.dump(SSs, f)
		await bot.send_message(ADMIN, f'rimosse {c} sessioni non valide')


async def addUsers(client, Users, group):
    global canAdd, AddedUsers, countusers, maxusers, tentativi
    AddedUsers = []
    tentativi = 0
    for user in Users:
        if maxusers == 0:
            if canAdd:
                AddedUsers.append(user)
                try:
                    await client(InviteToChannelRequest(group, [user]))
                    await asyncio.sleep(0.2)
                    countusers = countusers + 1
                except:
                    tentativi = tentativi + 1
                    pass
            else:
                break
        elif maxusers > 0 and countusers < maxusers:
            if canAdd:
                AddedUsers.append(user)
                try:
                    await client(InviteToChannelRequest(group, [user]))
                    await asyncio.sleep(0.2)
                    countusers = countusers + 1
                except:
                    tentativi = tentativi + 1
                    pass
            else:
                break


async def timeoutAdd(timeout):
    global canAdd
    await asyncio.sleep(timeout)
    canAdd = False


def saveraspintelligente():
    global raspingintelligentelist
    with open("raspaintelligentelist.json", "w+") as f:
        json.dump(raspingintelligentelist, f)


async def timeoutAdd(timeout):
    global canAdd
    await asyncio.sleep(timeout)
    canAdd = False


print("\033[92mdiminuire il controllo degli altri admin per le impostazioni seller?[Y/N]: (per argomento)")
try:
    controllolimitato = sys.argv[1].upper().startswith("Y")
except:
    controllolimitato = True
    print("controllo seller limitato: True, nessun argomento passato. es: python3 nomescript.py N")

bot = TelegramClient("bot", API_KEY, API_HASH)
archivialimitati = False


def raspacontrol():
    global raspingintelligentelist, ArchSSs
    R53 = False
    for voipdacontrollare in raspingintelligentelist:
        try:
            if datetime.now().date() > datetime.strptime(raspingintelligentelist[voipdacontrollare],
                                                         '%d/%m/%Y %H:%M').date():
                R53 = True
                SSs[voipdacontrollare] = ArchSSs[voipdacontrollare]
                saveSS()
                del (ArchSSs[voipdacontrollare])
                saveArchSS()
        except:
            pass
    return R53


@bot.on(events.NewMessage(incoming=True))
async def RaspaManager(e):
    global ADMIN, Getter, Number, TempClient, API_KEY, API_HASH, autoleave, ArchSSs, SSs, Grab, inAdding, canAdd, toadd, AddedUsers, ADMINS, controllolimitato, countusers, activeusers, maxusers, tentativi, archivialimitati, raspingintelligentelist, smspva_client, smspva_api, five_sim_api, five_sim_client, onlinesim_api, onlinesim_client, lines, path
    if True:
        if e.chat_id == ADMIN or e.chat_id in ADMINS:
            if e.text == "/start":

                Getter, Number, TempClient = None, None, None
                sdr = await e.get_sender()
                if smspva_api == "":
                    if raspacontrol():
                        await e.respond("**Benvenuto "+sdr.first_name+" \n**🧙 **Developer®** 🎩 @DebiruDansei 🎩 👋**Salve, sono il tuo raspabot personale, usa i bottoni per muoverti nelle immense funzionalià del** 🤖\n[☞ Guida](https://telegra.ph/AdderNet-GUIDA-08-20)", link_preview=False,
                                        buttons=[[Button.inline("☎️ Account ☎️", "voip")], [Button.inline("💡Voip Utility💡", "utility")], [Button.inline("📳Pannello smspa.com 📳", "smspva_panel")], [Button.inline("📲 Pannello 5sim.net 📲", "5sim_panel")],
                                                 [Button.inline("🥷 Ruba 🥷", "grab"), Button.inline(
                                                     "➕ Raspa ➕", "add")], [Button.inline("🗂 Carica File 🗂", "loadfile")],
                                                 [Button.inline("🛠️ mpostazioni 🛠️", "adminpanel"), Button.inline("🚪 JOIN 🚪", "join"), Button.inline("Cambia dispositivo", "changedevice")]])
                    else:
                        await e.respond("**Benvenuto "+sdr.first_name+" \n**🧙 **Developer®** 🎩 @DebiruDansei 🎩 👋**Salve, sono il tuo raspabot personale, usa i bottoni per muoverti nelle immense funzionalià del** 🤖\n[☞ Guida](https://telegra.ph/AdderNet-GUIDA-08-20)", link_preview=False,
                                        buttons=[[Button.inline("☎️ Account ☎️", "voip")], [Button.inline("💡Voip Utility💡", "utility")], [Button.inline("📳Pannello smspa.com 📳", "smspva_panel")], [Button.inline("📲 Pannello 5sim.net 📲", "5sim_panel")],
                                                 [Button.inline("🥷 Ruba 🥷", "grab"), Button.inline(
                                                     "➕ Raspa ➕", "add")], [Button.inline("🗂 Carica File 🗂", "loadfile")],
                                                 [Button.inline("🛠️ mpostazioni 🛠️", "adminpanel"), Button.inline("🚪 JOIN 🚪", "join"), Button.inline("Cambia dispositivo", "changedevice")]])
                else:
                    await e.respond("**Benvenuto "+sdr.first_name+" \n**🧙 **Developer®** 🎩 @DebiruDansei 🎩 👋**Salve, sono il tuo raspabot personale, usa i bottoni per muoverti nelle immense funzionalià del** 🤖\n[☞ Guida](https://telegra.ph/AdderNet-GUIDA-08-20)", link_preview=False,
                                    buttons=[[Button.inline("☎️ Account ☎️", "voip")], [Button.inline("💡Voip Utility💡", "utility")], [Button.inline("📳Pannello smspa.com 📳", "smspva_panel")], [Button.inline("📲 Pannello 5sim.net 📲", "5sim_panel")],
                                                 [Button.inline("🥷 Ruba 🥷", "grab"), Button.inline(
                                                     "➕ Raspa ➕", "add")], [Button.inline("🗂 Carica File 🗂", "loadfile")],
                                                 [Button.inline("🛠️ mpostazioni 🛠️", "adminpanel"), Button.inline("🚪 JOIN 🚪", "join"), Button.inline("Cambia dispositivo", "changedevice")]])
            if e.text == "/stopsmspva":
                await e.respond("❌Fermato Correttamente", buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
                oz = open("smspva_start.txt", "w")
                oz.write("stop")
                oz.close()
                leggi="coglione"

            if e.text == "/stop":
                stop = False
                await e.respond("Fermato")
            elif Getter != None:
                if Getter == 0:
                    Getter = None
                    if not e.text in SSs:
                        if not e.text in ArchSSs:

                            TempClient = TMPTelegramClient(StringSession(), API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
                            await TempClient.connect()
                            try:
                                await TempClient.send_code_request(phone=e.text)
                                Number = e.text
                                Getter = 1
                                await e.respond("**📩 Inserisci Il Codice 📩**",
                                                buttons=[[Button.inline("❌ Annulla", "voip")]])
                            except PhoneNumberFloodError:
                                await e.respond("**❌ Troppi Tentativi! Prova con un altro numero ❌**",
                                                buttons=[[Button.inline("🔄 Riprova", "addvoip")]])
                            except:
                                await e.respond("**❌ Numero Non Valido ❌**",
                                                buttons=[[Button.inline("🔄 Riprova", "addvoip")]])
                        else:
                            await e.respond("**❌ Voip Archiviato! Riaggiungilo ❌**",
                                            buttons=[[Button.inline("📁 Voip Archiviati", "arch")],
                                                     [Button.inline("🔄 Riprova", "addvoip")]])
                    else:
                        await e.respond("**❌ Voip già aggiunto ❌**", buttons=[[Button.inline("🔄 Riprova", "addvoip")]])
                elif Getter == 1:
                    try:
                        eCode = e.text.replace(",", "")
                        await TempClient.sign_in(phone=Number, code=eCode)
                        SSs[Number] = StringSession.save(TempClient.session)
                        Getter, Number = None, None
                        saveSS()
                        await e.respond("**✅ Voip Aggiunto Correttamente ✅**",
                                        buttons=[[Button.inline("🔙 Indietro", "voip")]])
                    except SessionPasswordNeededError:
                        Getter = 2
                        await e.respond("**🔑 Inserisci La Password (2FA) 🔑**",
                                        buttons=[[Button.inline("❌ Annulla", "voip")]])
                    except:
                        try:
                            nome = ["ᏢᎥᎬᏒᎶᎥᎾᏒᎶᎥᎾ ̪͔͈̖͗́̌́̏̅ͮᴾᴳ ²⁰⁰¹", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "🄳🅁🄰🄺🄴", "𝖆𝖈𝖕𝖎𝖓𝖌𝖚𝖎𝖓𝖔𝖊💔𝖈𝖈𝖍𝖎𝖉𝖚𝖊𝖕𝖚𝖓𝖙𝖎 🍯", "🧊Heisenberg🧊",
    "👑𝕂𝕀ℕ𝔾👑", "𝖣㋛︎𝖭'𝖳 𝗣𝗔𝗡𝗜𝗖", "☾︎✰𝙰𝚣𝙸𝚣𝙱𝚎𝙺☾︎✰", "🔥 𝐓𝐨𝐫𝐞𝐭𝐭𝐨 𝐈𝐏𝐓𝐕 | ᶠᵃˢᵗ & ᴵᴾᵀᵛ 🔥", "GetPvPᴾˡᵃᵍᵘ🇦🇱"]
                            cognome = ["ᏢᎥᎬᏒᎶᎥᎾᏒᎶᎥᎾ ̪͔͈̖͗́̌́̏̅ͮᴾᴳ ²⁰⁰¹", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "🄳🅁🄰🄺🄴", "𝖆𝖈𝖕𝖎𝖓𝖌𝖚𝖎𝖓𝖔𝖊💔𝖈𝖈𝖍𝖎𝖉𝖚𝖊𝖕𝖚𝖓𝖙𝖎 🍯", "🧊Heisenberg🧊",
    "👑𝕂𝕀ℕ𝔾👑", "𝖣㋛︎𝖭'𝖳 𝗣𝗔𝗡𝗜𝗖", "☾︎✰𝙰𝚣𝙸𝚣𝙱𝚎𝙺☾︎✰", "🔥 𝐓𝐨𝐫𝐞𝐭𝐭𝐨 𝐈𝐏𝐓𝐕 | ᶠᵃˢᵗ & ᴵᴾᵀᵛ 🔥", "GetPvPᴾˡᵃᵍᵘ🇦🇱"]
                            await TempClient.sign_up(e.text, first_name=random.choice(nome), last_name=random.choice(cognome))
                            SSs[Number] = StringSession.save(
                                TempClient.session)
                            await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                            setted = False
                            while not setted:
                                try:
                                    ran = "".join(random.choice(
                                        string.ascii_letters) for i in range(10))
                                    await TempClient(UpdateUsernameRequest(ran))
                                    setted = True
                                except Exception as e7:
                                    print(e7)
                                    await asyncio.sleep(10)
                                    pass
                            saveSS()

                            await e.respond("NUMERO OTTENUTO : " + Number,
                                            buttons=[[Button.inline("🔙 Indietro", "back")]])
                            Getter, Number = None, None
                        except Exception as e5:
                            print(e5)
                            Getter, Number = None, None
                            await e.respond("**❌ Codice Errato ❌**", buttons=[[Button.inline("🔄 Riprova", "addvoip")]])
                elif Getter == 800:
                    leggi = open("fivesim.txt", "r").read()
                    if leggi == "":
                        await e.respond("Si prega di impostare prima l'API KEY DAL PANNELLO 5sim.net", buttons=[[Button.inline("🔙 Indietro", "back")]])
                    else:
                        fivesim_api = leggi
                        country = e.text
                        headers = {
                        'Authorization': 'Bearer ' + fivesim_api,
                        'Accept': 'application/json',
                        }
                        try:
                            r = requests.get(
                                'https://5sim.net/v1/guest/products/' + country + '/' + "any", headers=headers)
                            json = json = r.json()
                            qnt = json["telegram"]["Qty"]
                            print(qnt)
                            scrivi = open("country.txt", "w")
                            scrivi.write(country)
                            scrivi.close()
                            await e.respond("settata correttamente", buttons=[[Button.inline("🔙 Indietro", "back")]])
                        except:
                            await e.respond("Nazione Incorretta\nSi prega di usare il nome inglese")
                elif Getter == 2:
                    try:
                        await TempClient.sign_in(phone=Number, password=e.text)
                        SSs[Number] = StringSession.save(TempClient.session)
                        Getter, Number = None, None
                        saveSS()
                        await e.respond("**✅ Numero Aggiunto Correttamente ✅**",
                                        buttons=[[Button.inline("🔙 Indietro", "voip")]])
                    except:
                        Getter, Number = None, None
                        await e.respond("**❌ Password Errata ❌**", buttons=[[Button.inline("🔄 Riprova", "addvoip")]])
                elif Getter == 3:
                    Getter = None
                    if e.text in SSs:
                        await e.respond(f"**🔧 Gestione »** `{e.text}`", buttons=[
                            [Button.inline("📁 Archivia", "arch;" + e.text)],

                            [Button.inline("👁️ Visualizza", "visualizza;" + e.text),
                             Button.inline("🔧 CAMBIA INFO", "setta;" + e.text)], [
                                Button.inline("➖ Rimuovi", "del;" + e.text)], [Button.inline("🔙 Indietro", "voip")]])
                    else:
                        await e.respond("**❌ Voip Non Trovato ❌**", buttons=[[Button.inline("🔄 Riprova", "voips")]])
                elif Getter == 600:

                    try:
                        money = getbalance(e.text)
                        await e.respond(f"Chiave API Settata correttamente\nSaldo Rilevato: {money}", buttons=[[Button.inline("🔙 Indietro", "back")]])
                        scrivi = open("fivesim.txt", "w")
                        scrivi.write(e.text)
                        scrivi.close()
                    except:
                        await e.respond("Chiave API INVALIDA,SI PREGA DI RIPROVARE", buttons=[[Button.inline("🔙 Indietro", "back")]])
                elif Getter == 4:
                    Getter = None
                    if e.text in ArchSSs:
                        await e.respond(f"**🔧 Gestione »** `{e.text}`", buttons=[
                            [Button.inline("➕ Riaggiungi", "add;" + e.text),
                             Button.inline("➖ Rimuovi", "delarch;" + e.text)], [Button.inline("🔙 Indietro", "voip")]])
                    else:
                        await e.respond("**❌ Voip Non Trovato ❌**", buttons=[[Button.inline("🔄 Riprova", "voips")]])
                elif Getter == 5:
                    Getter = None
                    Grab = e.text
                    banned = []
                    not_found = True
                    for SS in SSs:
                        if not_found:
                            try:

                                CClient = None
                                try:

                                    CClient = TMPTelegramClient(
                                        StringSession(SSs[SS]), API_KEY, API_HASH)
                                    await CClient.connect()
                                except:
                                    print("err")
                                    pass
                                if 1==1:
                                    try:
                                        ent = None
                                        prvt = False
                                        if "/joinchat/" in e.text and not "/+" in e.text:
                                            prvt = True
                                            st = e.text.split("/")
                                            group = st[len(st) - 1]
                                            try:
                                                ent = await CClient(ImportChatInviteRequest(group))
                                                print(ent.chats[0].id)
                                                ent = await CClient.get_entity(ent.chats[0].id)
                                            except FloodWaitError as err:
                                                await e.respond(
                                                    f"**⏳ Attendi altri {err.seconds} , il voip attuale {SS} sarà skippato. e passerò al prossimo voip dopo aver aspettato ⏳**")
                                                await asyncio.sleep(err.seconds + 4)
                                            except Exception as err:
                                                print(err)
                                                pass
                                        else:
                                            try:
                                                await CClient(JoinChannelRequest(e.text.replace("@", "")))
                                                ent = await CClient.get_entity(e.text.replace("@", ""))                                                
                                            except:
                                                pass
                                        try:
                                            users = await CClient.get_participants(
                                                ent.id,limit=2000)
                                            await asyncio.sleep(0.5)
                                            for User in users:                                                                                                
                                                try:
                                                    if not User.bot:
                                                        if activeusers:
                                                            accept = True
                                                            try:
                                                                if type(User.status).__name__ != "UserStatusRecently":
                                                                    accept = False
                                                                
                                                                    
                                                            except:
                                                                continue
                                                            if accept:
                                                                toadd.append(
                                                                    User)
                                                        else:
                                                            toadd.append(User)
                                                except:
                                                    pass
                                            if len(toadd) > 0:
                                                not_found = False

                                        except FloodWaitError as err:
                                            await e.edit(
                                                f"**⏳ Attendi altri {err.seconds} , il voip attuale sarà skippato. e passerò al prossimo voip dopo aver aspettato ⏳**")
                                            await asyncio.sleep(err.seconds + 4)
                                            pass
                                        if prvt:
                                            await CClient.delete_dialog(ent.id)
                                    except Exception as er:
                                        print(er)
                                        await e.respond(f"**⚠️ ATTENZIONE »** __Il voip__ `{SS}` __potrebbe essere stato bannato dal gruppo da cui prendere!__")
                                        banned.append(SS)
                                else:
                                    await e.respond(
                                        f"**clotshard")
                                    
                            except Exception as er:
                                print(er)
                                await e.respond(
                                    f"**⚠️ ATTENZIONE »** __Il voip__ `{SS}` __potrebbe essere stato bannato da telegram! Se l' hai solo disconnesso per errore riaggiungilo ;)__")
                                banned.append(SS)
                    if not_found:
                        await e.respond("**MEMBRI NON GRABBATI CORRETTAMENTE. RIPETERE.**",
                                        buttons=[[Button.inline("✔ Raspa", "add")],
                                                 [Button.inline("🔙 Indietro", "grab")]])
                    else:
                        await e.respond(f"**✅ Gruppo Impostato Correttamente ✅**\nGrabbati {len(toadd)}",
                                        buttons=[[Button.inline("✔ Raspa", "add")],
                                                 [Button.inline("🔙 Indietro", "grab")]])
                    
                elif Getter == 50:
                    if e.media != None:
                        path = await bot.download_media(e.media)
                        with open(path, "r+") as f:
                            import json
                            fil = json.load(f)

                        await e.respond("Caricato correttamente")
                        for x in fil:
                            if not x in SSs:

                                SSs[x] = fil[x]
                        saveSS()
                elif Getter == 51:
                    if e.text != None and e.text != "":
                        Getter = None
                        groups = e.text.split(" ")
                        tasks = []
                        for SS in SSs:

                            tasks.append(joinGroups(SS, groups))
                        msg = await e.respond("__Join In Corso...__\n\n**⚠️ » Per questa operazione possono essere necessarie anche ore o giorni!**")
                        await asyncio.gather(*tasks)
                        await msg.edit("**✅ Join Completato ✅**", buttons=[Button.inline("Indietro 🔙", "back")])
                    else:
                        await e.respond("**❌ Formato gruppi non valido ❌\n\nRiprovare 🔄**", buttons=[Button.inline("Annulla ❌", "back")])

                elif Getter == 6:
                    Getter = None
                    skipped = 0
                    inAdding = True
                    stayadd = True
                    Floodwait = 0
                    limitati = 0
                    raspata_i = 0
                    timer = datetime.now()
                    banned = []
                    limited = []
                    gruppo1_skipped = 0
                    gruppo2_skipped = 0
                    countusers = 0
                    msg = await e.respond(
                        "**✅ Aggiunta Membri In Corso ✅**\nATTENDI " +
                        str(len(SSs) * 125) + " secondi (circa)..",
                        buttons=[[Button.inline("❌ Interrompi", "stop")]])

                    for SS in SSs:
                        CClient = None
                        try:

                            CClient = TMPTelegramClient(
                                StringSession(SSs[SS]), API_KEY, API_HASH)
                            await CClient.connect()
                            if await CClient.get_me():
                                tentativi = 0
                                add = 0

                                try:
                                    channel = True
                                    prvt = False
                                    ent = None
                                    if "/joinchat/" in e.text and not "/+" in e.text:
                                        prvt = True
                                        st = e.text.split("/")
                                        group = st[len(st) - 1]
                                        try:
                                            ent = await CClient(ImportChatInviteRequest(group))
                                            print(ent.chats[0].id)
                                            ent = await CClient.get_entity(ent.chats[0].id)
                                        except FloodWaitError as err:
                                            await e.respond(
                                                f"**⏳ Attendi altri {err.seconds} secondi, il voip attuale {SS} sarà skippato. e passerò al prossimo voip dopo aver aspettato ⏳**")
                                            await asyncio.sleep(err.seconds + 4)
                                            pass
                                        except Exception as err:
                                            print(err)
                                            pass
                                        channel = False
                                        print(ent)
                                        if isinstance(ent, Channel):
                                            channel = True
                                    else:
                                        try:
                                            text = e.text.replace("@", "").replace("https://", "").replace(
                                                "http://", "").replace("t.me/", "")
                                            await CClient(JoinChannelRequest(text))
                                            ent = await CClient.get_entity(text)
                                        except Exception as eer:
                                            print(eer)
                                    try:
                                        await asyncio.sleep(0.5)
                                        users2 = await CClient.get_participants(
                                            ent.id,limit=2000)
                                        with open("databaseblack.db", "r") as f:
                                            users3 = f.readlines()
                                            for User in users2:
                                                try:
                                                    if User.username in toadd:
                                                        toadd.remove(User)
                                                except:
                                                    pass
                                            for User in toadd:
                                                try:
                                                    if User.username in users3 or User.username + '\n' in users3:
                                                        toadd.remove(User)
                                                except:
                                                    pass

                                        await asyncio.sleep(0.5)
                                        print(len(toadd))
                                        print(toadd)
                                        multi_i = 1
                                        multi_i2 = 2
                                        stayadd = True
                                        while raspata_i < len(toadd) and stayadd:
                                            print(raspata_i)
                                            user = toadd[raspata_i].username
                                            print(user)
                                            try:
                                                if tentativi < maxusers * 7 and add < maxusers:
                                                    try:
                                                        if channel:
                                                            multi_add = False
                                                            if multi_add:
                                                                user1 = toadd[raspata_i].username
                                                                user2 = toadd[len(
                                                                    toadd) - multi_i2].username
                                                                user3 = toadd[len(
                                                                    toadd) - multi_i2*multi_i].username
                                                                await CClient(
                                                                    InviteToChannelRequest(ent, [user1, user2, user3]))
                                                            else:
                                                                await CClient(
                                                                    InviteToChannelRequest(ent, [user]))

                                                        else:
                                                            await CClient(AddChatUserRequest(
                                                                ent,
                                                                user,
                                                                fwd_limit=10
                                                            ))
                                                        await asyncio.sleep(0.4)
                                                        add += 1
                                                        countusers += 1
                                                    except FloodWaitError as err:
                                                        stayadd = False
                                                        limited.append(SS)
                                                        date2 = datetime.now()
                                                        date2 += timedelta(
                                                            seconds=err.seconds + 40)
                                                        raspingintelligentelist[SS] = date2.strftime(
                                                            '%d/%m/%Y %H:%M')
                                                        Floodwait += 1
                                                    except:
                                                        if 3 < add < 7 and tentativi < 4:
                                                            with open(
                                                                    "databaseblack.db",
                                                                    "a") as f:
                                                                f.write(
                                                                    user + "\n")
                                                        tentativi += 1
                                                elif maxusers == 0:
                                                    if tentativi < 300:
                                                        try:
                                                            if channel:
                                                                multi_add=False
                                                                if multi_add:
                                                                    user1 = toadd[raspata_i].username
                                                                    user2 = toadd[len(
                                                                        toadd) - multi_i2].username
                                                                    user3 = toadd[
                                                                        len(toadd) - multi_i2 * multi_i].username
                                                                    await CClient(
                                                                        InviteToChannelRequest(ent,
                                                                                               [user1, user2, user3]))
                                                                else:
                                                                    await CClient(
                                                                        InviteToChannelRequest(ent, [user]))

                                                            else:
                                                                await CClient(AddChatUserRequest(
                                                                    ent,
                                                                    user,
                                                                    fwd_limit=10
                                                                ))
                                                            await asyncio.sleep(0.4)
                                                            add += 1
                                                            countusers += 1
                                                        except FloodWaitError as err:
                                                            Floodwait += 1
                                                            limited.append(SS)
                                                            date2 = datetime.now()
                                                            date2 += timedelta(
                                                                seconds=err.seconds + 40)
                                                            raspingintelligentelist[SS] = date2.strftime(
                                                                '%d/%m/%Y %H:%M')
                                                            stayadd = False
                                                        except:
                                                            if 3 < add < 7 and tentativi < 4:
                                                                with open(
                                                                        "databaseblack.db",
                                                                        "a") as f:
                                                                    f.write(
                                                                        user + "\n")
                                                            tentativi += 1
                                                    else:
                                                        stayadd = False
                                                else:
                                                    stayadd = False
                                            except FloodWaitError as err:
                                                await e.respond(
                                                    f"**⏳ Attendi altri {err.seconds} secondi, il voip attuale {SS} sarà skippato. e passerò al prossimo voip dopo aver aspettato ⏳**")
                                                await asyncio.sleep(err.seconds + 4)
                                            except:
                                                pass
                                            raspata_i += 1

                                        spambotchat = await CClient.get_entity("spambot")
                                        await CClient.send_message(spambotchat, "/start")
                                        messaggiospambot = await CClient.get_messages(spambotchat, limit=1)
                                        try:
                                            if "free" in messaggiospambot[0].message or "libero" in \
                                                    messaggiospambot[0].message:
                                                print("voip libero!")
                                            else:
                                                print(
                                                    "voip limitato!! 3 giorni!!")
                                                limited.append(SS)
                                                limitati += 1

                                                try:
                                                    start = messaggiospambot[0].message.index(
                                                        "account is now limited until ") + len(
                                                        "account is now limited until ")
                                                    end = messaggiospambot[0].message.index(" UTC",
                                                                                            start)
                                                    e6 = messaggiospambot[0].message[start:end]
                                                    date2 = datetime.strptime(
                                                        e6, '%d %b %Y, %H:%M')
                                                    date2 += timedelta(hours=1)
                                                    raspingintelligentelist[SS] = date2.strftime(
                                                        '%d/%m/%Y %H:%M')
                                                except:
                                                    try:
                                                        start = messaggiospambot[0].message.index(
                                                            "limitato fino al ") + len(
                                                            "limitato fino al ")
                                                        end = messaggiospambot[0].message.index(" UTC",
                                                                                                start)
                                                        e6 = messaggiospambot[0].message[start:end]
                                                        date2 = datetime.strptime(
                                                            e6, '%d %b %Y, %H:%M')
                                                        date2 += timedelta(hours=1)
                                                        raspingintelligentelist[SS] = date2.strftime(
                                                            '%d/%m/%Y %H:%M')
                                                    except:
                                                        date2 = datetime.now()
                                                        date2 += timedelta(days=3)
                                                        raspingintelligentelist[SS] = date2.strftime(
                                                            '%d/%m/%Y %H:%M')
                                                        print(
                                                            "error, setting 3 days")

                                        except Exception as e5:
                                            print(e5)

                                    except Exception as Er:
                                        print(Er)
                                    if prvt or autoleave:
                                        await CClient.delete_dialog(ent.id)
                                except Exception as Er:
                                    pass

                            else:
                                pass
                        except:
                            pass
                    now = datetime.now() - timer
                    now2 = now.total_seconds()
                    if archivialimitati:
                        if limited.__len__() > 0:
                            for n2 in limited:
                                if n2 in SSs:
                                    if not n2 in ArchSSs:
                                        ArchSSs[n2] = SSs[n2]
                                        saveArchSS(e.chat_id)
                                    del (SSs[n2])
                                    saveSS(e.chat_id)

                    if banned.__len__() > 0:
                        for n in banned:
                            if n in SSs:
                                del (SSs[n])
                        saveSS(e.chat_id)
                    inAdding = False
                    if gruppo2_skipped > gruppo1_skipped:
                        await msg.edit(
                            f"**✅ Aggiunta Membri Completata ✅**\nin ⌛ {'{:.2f}'.format(now2)} __secondi.__" + "\nAggiunti: " + str(
                                countusers) + "  ⏳⏳⏳  su un massimo di : " + str(
                                maxusers) + "\n\n📱Voip skippati (in floodwait) : " + str(
                                Floodwait) + " su " + str(
                                len(SSs) + limitati) + "\n♨️Voip limitati : " + str(limitati) + " su " + str(len(
                                    SSs) + limitati) + "\n\n🔬DIAGNOSI: la problematica maggiore è sul secondo gruppo.\n🤗consiglio: non sono compatibili gruppi privati, o canali." + "\nADDING INTELLIGENTE🧠 is: " + str(
                                archivialimitati),
                            buttons=[[Button.inline("🔙 Indietro", "back")]])
                    elif gruppo1_skipped > gruppo2_skipped:
                        await msg.edit(
                            f"**✅ Aggiunta Membri Completata ✅**\nin ⌛ {'{:.2f}'.format(now2)} __secondi.__" + "\nAggiunti: " + str(
                                countusers) + "  ⏳⏳⏳  su un massimo di : " + str(
                                maxusers) + "\n\n📱Voip skippati (in floodwait) : " + str(
                                Floodwait) + " su " + str(len(
                                    SSs) + limitati) + "\n♨️Voip limitati : " + str(limitati) + " su " + str(len(
                                        SSs) + limitati) + "\n\n🔬DIAGNOSI: la problematica maggiore è sul primo gruppo.\n🤗consiglio: non sono compatibili gruppi privati, o canali." + "\nADDING INTELLIGENTE🧠 is: " + str(
                                archivialimitati),
                            buttons=[[Button.inline("🔙 Indietro", "back")]])
                    else:
                        await msg.edit(
                            f"**✅ Aggiunta Membri Completata ✅**\nin ⌛ {'{:.2f}'.format(now2)} __secondi.__" + "\nAggiunti: " + str(
                                countusers) + "  ⏳⏳⏳  su un massimo di : " + str(
                                maxusers) + "\n\n📱Voip skippati (in floodwait) : " + str(
                                Floodwait) + " su " + str(len(
                                    SSs) + limitati) + "\n♨️Voip limitati : " + str(limitati) + " su " + str(len(
                                        SSs) + limitati) + "\nADDING INTELLIGENTE🧠 is: " + str(archivialimitati),
                            buttons=[[Button.inline("🔙 Indietro", "back")]])
                    with open(f"raspaintelligentelist{chat_id}.json", "w+") as f:
                        json.dump(raspingintelligentelist, f)
                elif Getter == 9:
                    Getter = None
                    try:
                        await TempClient(UpdateUsernameRequest(e.text))
                        await e.respond("✅Username settato✅",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                    except:
                        await e.respond("❌username non valido/disponibile❌!\nusername non settato!",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                elif Getter == 9:
                    Getter = None
                    try:
                        await TempClient(UpdateUsernameRequest(e.text))
                        await e.respond("✅Username settato✅",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                    except:
                        await e.respond("❌username non valido/disponibile❌!\nusername non settato!",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                elif Getter == 10:
                    Getter = None
                    try:
                        path = await bot.download_media(e.media)
                        print(path)
                        await TempClient(UploadProfilePhotoRequest(
                            await TempClient.upload_file(path)
                        ))
                        await e.respond("✅foto settata✅",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                    except Exception as e:
                        print(str(e))
                        await e.respond("❌foto non settata❌!\nerrore nel formato foto!",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                elif Getter == 12:
                    Getter = None
                    try:
                        await TempClient(UpdateProfileRequest(
                            first_name=e.text
                        ))
                        await e.respond("✅nome settato✅",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                    except:
                        await e.respond("❌nome non settato❌!\nerrore nel nome inserito!",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                elif Getter == 13:
                    Getter = None
                    try:
                        await TempClient(UpdateProfileRequest(
                            last_name=e.text
                        ))
                        await e.respond("✅cognome settato✅",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                    except:
                        await e.respond("❌cognome non settato❌!\nerrore nel cognome inserito!",
                                        buttons=[[Button.inline("🔙 Indietro", "back")]])
                elif Getter == 14:
                     
                    apis=open("smspva.txt","w")
                    apis.write(e.text)
                    apis.close()
                    a=open("smspva.txt","r")
                    smspva_api=a.read()
                    
                    await e.respond("**chiave api settata**",
                                    buttons=[
                                        [Button.inline("🔙 Indietro", "makevoip")]])
                elif Getter == 80:
                    testo=e.text
                    osas = open("fivesim.txt","w")
                    osas.write(testo)
                    osas.close()
				    
                    await e.respond("**chiave api settata**",
                                    buttons=[
                                        [Button.inline("🔙 Indietro", "makevoip")]])
                elif Getter == 17:
                    onlinesim_api = e.text
                    onlinesim_client = onlinesim(e.text)
                    await e.respond("**chiave api settata**",
                                    buttons=[
                                        [Button.inline("🔙 Indietro", "makevoip")]])

                elif Getter == 19 and e.chat_id == ADMIN:
                    Getter = None
                    maxusers = int(e.text)
                    maxusers == 0
                        
                    await e.respond("utenti massimi settati a: " + str(maxusers),
                                    buttons=[[Button.inline("🔙 Indietro", "back")]])

            else:
                text1 = e.text.split(" ")
                try:
                    if "/admin" in text1[0] and e.chat_id == ADMIN:
                        ADMINS.append(int(text1[1]))
                        await e.respond("👮‍♂️ Reso admin 👮‍♂️" + text1[1])
                    elif "/unadmin" in text1[0] and e.chat_id == ADMIN:
                        ADMINS.remove(int(text1[1]))
                        await e.respond("👮‍♂️ Rimosso admin 👮‍♂️" + text1[1])
                except Exception as e4:
                    print(e4)


@bot.on(events.CallbackQuery())
async def callbackQuery(e):
    global ADMIN, Getter, Number, TempClient, API_KEY, API_HASH, ArchSSs, SSs, Grab, inAdding, headers, nome, cognome, ADMINS, controllolimitato, oidocrop, activeusers, maxusers, archivialimitati, raspingintelligentelist, smspva_api, smspva_client, five_sim_api, five_sim_client, onlinesim_api, onlinesim_client, path, stop
    if e.sender_id == ADMIN or e.sender_id in ADMINS:
        Eurl = "https://picsum.photos/id/237/200/300"
        headerss = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        req = urllib.Request(url=Eurl, headers=headerss)
        fd = urllib.urlopen(req)
        image_file = io.BytesIO(fd.read())
        image = Image.open(image_file)
        image.save("immagine.jpg")
        if e.data == b"back":
            Getter, Number, TempClient = None, None, None
            sdr = await e.get_sender()
            if smspva_api == "":
                await e.edit("**Benvenuto "+sdr.first_name+" \n**🧙 **Developer®** 🎩 @DebiruDansei 🎩 👋**Salve, sono il tuo raspabot personale, usa i bottoni per muoverti nelle immense funzionalià del** 🤖\n[☞ Guida](https://telegra.ph/AdderNet-GUIDA-08-20)", link_preview=False,buttons=[[Button.inline("☎️ Account ☎️", "voip")], [Button.inline("💡Voip Utility💡", "utility")], [Button.inline("📳Pannello smspa.com 📳", "smspva_panel")], [Button.inline("📲 Pannello 5sim.net 📲", "5sim_panel")],
                                                 [Button.inline("🥷 Ruba 🥷", "grab"), Button.inline(
                                                     "➕ Raspa ➕", "add")], [Button.inline("🗂 Carica File 🗂", "loadfile")],
                                                 [Button.inline("🛠️ mpostazioni 🛠️", "adminpanel"), Button.inline("🚪 JOIN 🚪", "join"), Button.inline("Cambia dispositivo", "changedevice")]])
            else:
                
                await e.edit("**Benvenuto "+sdr.first_name+" \n**🧙 **Developer®** 🎩 @DebiruDansei 🎩 👋**Salve, sono il tuo raspabot personale, usa i bottoni per muoverti nelle immense funzionalià del** 🤖\n[☞ Guida](https://telegra.ph/AdderNet-GUIDA-08-20)", link_preview=False,buttons=[[Button.inline("☎️ Account ☎️", "voip")], [Button.inline("💡Voip Utility💡", "utility")], [Button.inline("📳Pannello smspa.com 📳", "smspva_panel")], [Button.inline("📲 Pannello 5sim.net 📲", "5sim_panel")],
                                                 [Button.inline("🥷 Ruba 🥷", "grab"), Button.inline(
                                                     "➕ Raspa ➕", "add")], [Button.inline("🗂 Carica File 🗂", "loadfile")],
                                                 [Button.inline("🛠️ mpostazioni 🛠️", "adminpanel"), Button.inline("🚪 JOIN 🚪", "join"), Button.inline("Cambia dispositivo", "changedevice")]])
        elif e.data==b"smspva_panel":
            try:       
                leggi=open("smspva.txt","r").read()         
                money=getbalancesms(leggi)
            except:
                money="API KEY NON IMPOSTATA"
                    
            await e.edit(f"📱Benvenuto nel pannello di SMSPVA.COM\nNazione Default: __Italia__\nSaldo: {money} ",buttons=[[Button.inline("⚒ Imposta API KEY ⚒","smspvaset")],[Button.inline("♻️ Avvia Creazione ♻️","smspva_start")],[Button.inline("🔙 Indietro 🔙", "back")]])                
        elif e.data==b"5sim_panel":
            try:       
                leggi=open("fivesim.txt","r").read()         
                money=getbalance(leggi)
            except:
                money="API KEY NON IMPOSTATA"
                    
            await e.edit(f"📱 Benvenuto nel pannello di 5SIM.NET\nSaldo: {money} ",buttons=[[Button.inline("⚒ Imposta API KEY ⚒","set_5simapi")],[Button.inline("🇦🇮 Imposta Nazione 🇦🇮","set_country")],[Button.inline("♻️ Avvia Creazione ♻️","5sim")],[Button.inline("🔙 Indietro", "back")]])
        elif e.data==b"set_5simapi":
            await e.edit("Inserisci L'api key di 5SIM.NET\nSe non sai come ottenerla,leggi [qui](https://telegra.ph/AdderNet-GUIDA-08-20)", link_preview=False, buttons=[[Button.inline("🔙 Indietro", "5sim_panel")]])
            aps=open("fivesim.txt","r").read()
            Getter=600
        elif e.data==b"set_country":
            await e.edit("Inserisci la nazione:", buttons=[[Button.inline("🔙 Indietro", "back")]])
            Getter=800    

                    
            
        elif e.data == b"utility":
            await e.edit(buttons=[[Button.inline("🚨 Check Limitati 🚨", "nolimit")], [Button.inline("🖇️ Disarchivia Tutti 🖇️", "disarchivia")],[Button.inline("🗂 Archivia Tutti 🗂", "archiviaall")], [Button.inline("🦀 Check Voip 🦀", "checkvoips")],[Button.inline("🔙 Indietro 🔙", "back")]])
        elif e.data == b"join":

            Getter = 51
            await e.edit("__👥 Inviare la lista di gruppi in cui entrare!__", buttons=[Button.inline("Annulla ❌", "back")])
        elif e.data == b"checkvoips":
            await removeinv()

            await bot.send_message(ADMIN, "OPERAZIONE TERMINATA")
        elif e.data == b"loadfile":
            await e.edit("Invia il file JSON dei voip da caricare")  
            Getter = 50
		    
			  
        elif e.data == b"adminpanel":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                await e.edit("scegli un opzione:", buttons=[[Button.inline("🌀 Solo Attivi 🌀", "attiviset")],[Button.inline("📳 Ottieni File Voip 📳", "getSSS")],[Button.inline("🔙 Indietro 🔙", "back")]])
        elif e.data == b"maxutentiset":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                Getter = 19
                await e.edit("inserisci un numero utenti:", buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
        elif e.data == b"disarchivia":
            for SS in list(ArchSSs):
               if not SS in SSs:
                   SSs[SS] = ArchSSs[SS]
                   saveSS()
                   del (ArchSSs[SS]) 
                   saveArchSS()
            await e.respond("Disarchiviati tutti i voip")  
        elif e.data == b"archiviaall":
            for SS in list(SSs):
               if not SS in ArchSSs:
                   ArchSSs[SS] = SSs[SS]
                   saveArchSS()
                   del (SSs[SS]) 
                   saveSS()
            await e.respond("Archiviati tutti i voip")                     
        elif e.data == b"nolimit":
            lomitati=0  
            await e.edit("🕵️ **Sto controllando** 🕵️")
            for SS in list(SSs):
                try:
                    client = TMPTelegramClient(StringSession(SSs[SS]), API_KEY, API_HASH)
                    await client.connect()
                    spambotchat = await client.get_entity("spambot")
                    await client.send_message(spambotchat, "/start")   
                    await asyncio.sleep(1)             
                    messaggiospambot = await client.get_messages(spambotchat, limit=1)
                    mex=messaggiospambot[0].message.split(" ")
                    if "afraid" in mex:
                        lomitati=lomitati+1
                    
                        if not SS in ArchSSs:
                            ArchSSs[SS] = SSs[SS]
                            saveArchSS()
                            del (SSs[SS])
                            saveSS()
                    else:
                        print(mex)  
                except:
                    pass        
            await e.respond(f"ci sono {lomitati} voip limitati")          
                  
        elif e.data == b"readd":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                raspcontrollo = raspacontrol()
                await e.answer("DEI VOIP SONO STATI RIAGGIUNTI?🧠 is: " + str(raspcontrollo), alert=True)
        elif e.data == b"limitinfo":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                for data4 in raspingintelligentelist:
                    await e.client.send_message(e.sender_id, "il voip " + data4 + " sarà slimitato il : " + raspingintelligentelist[data4])
                await e.client.send_message(e.sender_id, "**INFO OTTENUTE.\n(se non hai ottenuto nulla, non hai voip attualmente limitati REGISTRATI NEL BOT)\n\n🤖 Pannello Raspa Bot\n\n⚙ Versione » 4.4**",
                                            buttons=[[Button.inline("📞 Voip", "voip")],
                                                     [Button.inline("🥷 Ruba 🥷", "grab"), Button.inline(
                                                         "➕ Raspa ➕", "add")], [Button.inline("🗂 Carica File 🗂", "loadfile")],
                                                     [Button.inline("🛠️ Impostazioni 🛠️", "adminpanel")]])
        elif e.data == b"limitatiset":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                archivialimitati = not archivialimitati
                await e.answer("🧠 ADDING INTELLIGENTE  🧠 is: " + str(archivialimitati), alert=True)
        elif e.data == b"attiviset":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                activeusers = not activeusers
                await e.answer("solo attivi is: " + str(activeusers), alert=True)

        elif e.data == b"getSSS":
            if controllolimitato and e.sender_id != ADMIN:
                await e.answer("non hai la possibilità di accedervi.. \ncontrollo limitato.", alert=True)
            else:
                await e.respond("ecco il FILE VOIP📳", file="SSs.json", buttons=[
                    [Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"stop":
            await e.edit("**✅ Aggiunta Interrotta ✅**", buttons=[[Button.inline("🔙 Indietro", "back")]])
            python = sys.executable
            if controllolimitato:
                os.execl(python, python, *sys.argv, "Y")
            else:
                os.execl(python, python, *sys.argv, "N")
        elif inAdding:
            await e.answer("❌» Questa sezione è in creazione!", alert=True)
        elif e.data == b"makevoip":
            Getter = None
            
            
            await e.edit("**SELEZIONA UNA PIATTAFORMA  : **",
                             buttons=[[Button.inline("SMSPVA", "smspva")],[
                                 Button.inline("cambia chiavi API", "makevoipsettings")],
                                 [Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"makevoipsettings":
            

            await e.edit("**SELEZIONA LA PIATTAFORMA **",
                             buttons=[[Button.inline("SMSPVA", "smspvaset")],
                                      [Button.inline("🔙 Indietro", "back")]])

        elif e.data == b"smspvaset":
            Getter = 14
            await e.edit("**INVIA CHIAVE API SMSPVA.COM**",
                         buttons=[[Button.inline("🔙 Indietro", "smspva_panel")]])
        elif e.data == b"5sim":
            fivesim_api=open("fivesim.txt","r").read()
            
            if fivesim_api == "":
                    Getter = 80
                    await e.edit("Per continuare inserisci la tua API KEY di 5SIM.NET")
            else:
                fivesimm=open("fivesim_start.txt","w")
                fivesimm.write("start")
                fivesimm.close() 
                leggi=open("fivesim_start.txt","r").read()
                fivesim_api=open("fivesim.txt","r").read()
                country=open("country.txt","r").read()
                if country=="":
                    country = "venezuela"
                operator = "any"
                product = 'telegram'
                
                headers = {
                    'Authorization': 'Bearer ' + fivesim_api,
                    'Accept': 'application/json',
                }
                
                await e.edit("💰Sto comprando i Voip", buttons=[[Button.inline("❌Ferma", "stop_5sim")]])
                while leggi=="start":
                    leggi = open("fivesim_start.txt", "r").read()
                    fivesim_api=open("fivesim.txt","r").read()                                        
                    codice=False                     
                    r = requests.get(
                        'https://5sim.net/v1/guest/products/' + country + '/' + operator, headers=headers)
                    jsonn= r.json()
                    qnt = jsonn["telegram"]["Qty"]
                    if qnt != 0:
                        tentativo = 0
                        attivazione = True
                        
                        
                                               
                        while attivazione:
                            tentativo = tentativo+1
                            if tentativo == 30:
                                await e.respond("probabilmente non sono disponibili voip")
                                leggi="ci"
                                break
                            
                            r = requests.get('https://5sim.net/v1/user/buy/activation/' +
                                             country + '/' + operator + '/' + product, headers=headers)
                            await asyncio.sleep(5)                                                                                   
                            try:
                                jsonn = r.json()
                                numero = jsonn["phone"]
                                print(numero)
                                id = jsonn["id"]

                                attivazione = False
                            except:
                                pass

                            if attivazione == False:
 
                                try:
                                    TempClient = TMPTelegramClient(StringSession(), API_KEY, API_HASH)
                                    await TempClient.connect()
                                    await TempClient.send_code_request(phone=numero)
                                    attivazione = False
                                    codice=True
                                except PhoneNumberBannedError:
                                    r = requests.get(
                                        'https://5sim.net/v1/user/cancel/' + str(id), headers=headers)
                                    
                                    
                                except:                                                                            
                                    r = requests.get('https://5sim.net/v1/user/cancel/' + str(id), headers=headers)
                                    
                                          

                        #CODE
                        
                        tentativi = 0
                        while codice:
                            print("cod")
                            await asyncio.sleep(10)                            
                            if tentativi == 20:
                                
                                re = requests.get('https://5sim.net/v1/user/cancel/' + str(id), headers=headers)
                                codice=False

                            tentativi = tentativi+1
                            r = requests.get(
                                'https://5sim.net/v1/user/check/' + str(id), headers=headers)
                            try:
                                jsonn = r.json()
                                sms = jsonn["sms"]
                                for message in sms:
                                    cod = message["code"]
                                    

                                if len(sms) != 0:

                                    await TempClient.sign_up(cod, first_name=random.choice(nome), last_name=random.choice(cognome))
                                    SSs[numero] = StringSession.save(TempClient.session)
                                    saveSS()
                                    me = await TempClient.get_me()

                                    
                                    await TempClient(UpdateUsernameRequest(me.first_name+str(me.id)))
                                    me = await TempClient.get_me()
                                    
                                    await e.respond(f"NUMERO OTTENUTO : {numero}\nℹ️Info: \nNome: {me.first_name}\nCognome: {me.last_name}\nID {me.id}\nLink: [{me.first_name}](https://t.me/{me.username})",link_preview=False, buttons=[[Button.inline("❌Ferma", "stop_5sim")]])
                                                                                

                                    codice = False
                            except:
                                pass

                    else:
                        await e.edit("Al momento i numeri sono esauriti")
        elif e.data==b"stop_5sim":
            await e.edit("❌Fermato Correttamente", buttons=[[Button.inline("🔙 Indietro", "back")]])
            scrivi=open("fivesim_start.txt","w")
            scrivi.write("fermo")
            scrivi.close()
            leggi="stop"
                            

        elif e.data==b"stop_smspva": 
            await e.edit("❌Fermato Correttamente", buttons=[[Button.inline("🔙 Indietro", "back")]])
            oz=open("smspva_start.txt","w")
            oz.write("stop")
            oz.close()
            leggi="cicalo" 
                          
        elif e.data==b"smspva_start":
                oz=open("smspva_start.txt","w")
                oz.write("start")
                oz.close() 
                leggi=open("smspva_start.txt","r").read()
                smspva_api=open("smspva.txt","r").read()
                
                countrysms = "RO"

                
                await e.edit("💰Sto comprando i Voip",buttons=[[Button.inline("ferma","stop_smspva")]])
                tentativo = 0
                while leggi=="start":
                    leggi = open("smspva_start.txt", "r").read()
                    fivesim_api=open("smspva.txt","r").read()                                        
                    codice=False   

                    r = requests.get(
                        f"http://smspva.com/priemnik.php?metod=get_count_new&service=opt29&apikey={smspva_api}&country={countrysms}")
                    js = r.json()

                    if js["online"] != 0:
                        ordine = True
                        tentativo = 0
                        while ordine:
                            tentativo = tentativo+1   
                            if tentativo==30:
                                await e.respond("probabilmente non sono disponibili voip ora")
                                leggi="co"
                                break                                                     
                            r = requests.get(
                                f"http://smspva.com/priemnik.php?metod=get_number&country={countrysms}&service=opt29&apikey={smspva_api}")
                            print(r.text)
                            jsonn = r.json()
                            if jsonn["response"] == "1":

                                id = jsonn["id"]
                                numero = jsonn["CountryCode"]+jsonn["number"]
                                try:
                                    TempClient = TMPTelegramClient(StringSession(), API_KEY, API_HASH)
                                    await TempClient.connect()
                                    await TempClient.send_code_request(phone=numero)
                                    attivazione = False
                                    codice=True
                                    ordine=False
                                except PhoneNumberBannedError:
                                    try:
                                        id = jsonn["id"]
                                        r = requests.get(
                                            f"http://smspva.com/priemnik.php?metod=denial&country={countrysms}&service=opt29&id={id}&apikey={smspva_api}")
                                        jsonn = r.json()

                                        if jsonn["response"] == "1":
                                            print("rimborso bannato")

                                    except:
                                        pass
                                                                        
                                except: 
                                    r = requests.get(f"http://smspva.com/priemnik.php?metod=denial&country={countrysms}&service=opt29&id={id}&apikey={smspva_api}")    
                                                                                                           
                                    
                                    
                            else:  # cancel order
                                print("cancello")
                                try:
                                    id = jsonn["id"]
                                    r = requests.get(
                                        f"http://smspva.com/priemnik.php?metod=denial&country={countrysms}&service=opt29&id={id}&apikey={smspva_api}")
                                    jsonn = r.json()
                                    if jsonn["response"] == "1":
                                        print("else")
                                    else:
                                        pass
                                except:
                                    pass

                        #CODE
                        
                        tentativi = 0
                        while codice:
                            print("cod")
                            await asyncio.sleep(10)                            
                            if tentativi == 20:
                                
                                r = requests.get(
                                    f"http://smspva.com/priemnik.php?metod=denial&country={countrysms}&service=opt29&id={id}&apikey={smspva_api}")
                                codice=False
                            tentativi = tentativi+1
                            r = requests.get(
                                f"http://smspva.com/priemnik.php?metod=get_sms&country={countrysms}&service=opt29&id={id}&apikey={smspva_api}")
                            jsonn = r.json()

                            if jsonn["response"] == "1":

                                code = jsonn["sms"]
                                print(code)
                                nome = ["ᏢᎥᎬᏒᎶᎥᎾᏒᎶᎥᎾ ̪͔͈̖͗́̌́̏̅ͮᴾᴳ ²⁰⁰¹", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "🄳🅁🄰🄺🄴", "𝖆𝖈𝖕𝖎𝖓𝖌𝖚𝖎𝖓𝖔𝖊💔𝖈𝖈𝖍𝖎𝖉𝖚𝖊𝖕𝖚𝖓𝖙𝖎 🍯", "🧊Heisenberg🧊",
    "👑𝕂𝕀ℕ𝔾👑", "𝖣㋛︎𝖭'𝖳 𝗣𝗔𝗡𝗜𝗖", "☾︎✰𝙰𝚣𝙸𝚣𝙱𝚎𝙺☾︎✰", "🔥 𝐓𝐨𝐫𝐞𝐭𝐭𝐨 𝐈𝐏𝐓𝐕 | ᶠᵃˢᵗ & ᴵᴾᵀᵛ 🔥", "GetPvPᴾˡᵃᵍᵘ🇦🇱"]
                                cognome = ["ᏢᎥᎬᏒᎶᎥᎾᏒᎶᎥᎾ ̪͔͈̖͗́̌́̏̅ͮᴾᴳ ²⁰⁰¹", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "🄳🅁🄰🄺🄴", "𝖆𝖈𝖕𝖎𝖓𝖌𝖚𝖎𝖓𝖔𝖊💔𝖈𝖈𝖍𝖎𝖉𝖚𝖊𝖕𝖚𝖓𝖙𝖎 🍯", "🧊Heisenberg🧊",
    "👑𝕂𝕀ℕ𝔾👑", "𝖣㋛︎𝖭'𝖳 𝗣𝗔𝗡𝗜𝗖", "☾︎✰𝙰𝚣𝙸𝚣𝙱𝚎𝙺☾︎✰", "🔥 𝐓𝐨𝐫𝐞𝐭𝐭𝐨 𝐈𝐏𝐓𝐕 | ᶠᵃˢᵗ & ᴵᴾᵀᵛ 🔥", "GetPvPᴾˡᵃᵍᵘ🇦🇱"]
                                await TempClient.sign_up(code, first_name=random.choice(nome), last_name=random.choice(cognome))

                                SSs[numero] = StringSession.save(TempClient.session)
                                saveSS()
                                me = await TempClient.get_me()

                                
                                await TempClient(UpdateUsernameRequest(me.first_name+str(me.id)))
                                me = await TempClient.get_me()
                                
                                await e.respond(f"NUMERO OTTENUTO : {numero}\nℹ️Info: \nNome: {me.first_name}\nCognome: {me.last_name}\nID {me.id}\nLink: [{me.first_name}](https://t.me/{me.username})", link_preview=False, buttons=[[Button.inline("❌Ferma", "stop_smspva")]])
                                                                            

                                codice = False
                           

                    else:
                        await e.edit("Al momento i numeri sono esauriti")                                    
                        
        elif e.data == b"fivesim":
            if five_sim_api is None:
                await e.edit("**NESSUNA CHIAVE API **",
                             buttons=[[Button.inline("SET 5SIM APIKEY", "fivesimset")],
                                      [Button.inline("🔙 Indietro", "back")]])
            else:
                await e.edit("sto provando ad ottenere un voip..")
                order = five_sim_client.get_number("france", "telegram")
                if order is not None:
                    try:
                        number = "+33"+order["phone"].replace(" ", "")
                        TempClient = TMPTelegramClient(
                            StringSession(), API_KEY, API_HASH)
                        await TempClient.connect()
                        print(order["number"])
                        await TempClient.send_code_request(number)
                        tentativi = 0
                        Code = None
                        Limitator = True
                        while Limitator:
                            code = five_sim_client.Get_Code(order["id"])
                            if code is not None:
                                Code = code
                                Limitator = False
                            else:
                                tentativi = tentativi + 1
                                await asyncio.sleep(10)
                                if tentativi > 46:
                                    Limitator = False
                        if Code is not None:
                            await TempClient.sign_up(Code, first_name='ANNINO', last_name='Fragola')
                            SSs[number] = StringSession.save(
                                TempClient.session)
                            saveSS()
                            await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                            setted = False
                            while not setted:
                                try:
                                    ran = "".join(random.choice(
                                        string.ascii_letters) for i in range(10))
                                    await TempClient(UpdateUsernameRequest(ran))
                                    setted = True
                                except:
                                    await asyncio.sleep(10)
                                    pass
                            await e.edit("NUMERO OTTENUTO : " + number,
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])

                        else:
                            if five_sim_client.ban_number(order["id"]) is True:
                                await e.edit("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])
                            else:
                                await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])

                    except FloodWaitError as floderr:
                        await e.edit(f"**⏳ Attendi altri {floderr.seconds} ⏳*per il voip attuale sarà chiesto un rimborso.*", buttons=[[Button.inline("🔙 Indietro", "back")]])
                        if five_sim_client.ban_number(order["id"]) is True:
                            await e.respond("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                            buttons=[[Button.inline("🔙 Indietro", "back")]])
                        else:
                            await e.respond("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                            buttons=[[Button.inline("🔙 Indietro", "back")]])
                        await asyncio.sleep(floderr.seconds + 4)

                    except Exception as e6:
                        print(e6)
                        if five_sim_client.ban_number(order["id"]) is True:
                            await e.edit("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])
                        else:
                            await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])
                else:
                    order = five_sim_client.get_number("costarica", "telegram")
                    if order is not None:
                        try:
                            number = "+506"+order["phone"].replace(" ", "")
                            TempClient = TMPTelegramClient(
                                StringSession(), API_KEY, API_HASH)
                            await TempClient.connect()
                            await TempClient.send_code_request(number)
                            tentativi = 0
                            Code = None
                            Limitator = True
                            while Limitator:
                                code = five_sim_client.Get_Code(order["id"])
                                if code is not None:
                                    Code = code
                                    Limitator = False
                                else:
                                    tentativi = tentativi + 1
                                    await asyncio.sleep(10)
                                    if tentativi > 46:
                                        Limitator = False
                            if Code is not None:
                                await TempClient.sign_up(Code, first_name='ANNINO', last_name='Fragola')
                                SSs[number] = StringSession.save(
                                    TempClient.session)
                                saveSS()
                                await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                                setted = False
                                while not setted:
                                    try:
                                        ran = "".join(random.choice(
                                            string.ascii_letters) for i in range(10))
                                        await TempClient(UpdateUsernameRequest(ran))
                                        setted = True
                                    except:
                                        await asyncio.sleep(10)
                                        pass
                                await e.edit("NUMERO OTTENUTO : " + number,
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])

                            else:
                                if five_sim_client.ban_number(order["id"]) is True:
                                    await e.edit("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])
                                else:
                                    await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])

                        except FloodWaitError as floderr:
                            await e.edit(f"**⏳ Attendi altri {floderr.seconds} ⏳*per il voip attuale sarà chiesto un rimborso.*", buttons=[[Button.inline("🔙 Indietro", "back")]])
                            if five_sim_client.ban_number(order["id"]) is True:
                                await e.respond("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                                buttons=[[Button.inline("🔙 Indietro", "back")]])
                            else:
                                await e.respond("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                                buttons=[[Button.inline("🔙 Indietro", "back")]])
                            await asyncio.sleep(floderr.seconds + 4)

                        except Exception as e6:
                            print(e6)
                            if five_sim_client.ban_number(order["id"]) is True:
                                await e.edit("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])
                            else:
                                await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])
                    else:
                        order = five_sim_client.get_number(
                            "poland", "telegram")
                        if order is not None:
                            try:
                                number = "+48"+order["phone"].replace(" ", "")
                                TempClient = TMPTelegramClient(
                                    StringSession(), API_KEY, API_HASH)
                                await TempClient.connect()
                                await TempClient.send_code_request(number)
                                tentativi = 0
                                Code = None
                                Limitator = True
                                while Limitator:
                                    code = five_sim_client.Get_Code(
                                        order["id"])
                                    if code is not None:
                                        Code = code
                                        Limitator = False
                                    else:
                                        tentativi = tentativi + 1
                                        await asyncio.sleep(10)
                                        if tentativi > 46:
                                            Limitator = False
                                if Code is not None:
                                    await TempClient.sign_up(Code, first_name='ANNINO', last_name='Fragola')
                                    SSs[number] = StringSession.save(
                                        TempClient.session)
                                    saveSS()
                                    await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                                    setted = False
                                    while not setted:
                                        try:
                                            ran = "".join(random.choice(
                                                string.ascii_letters) for i in range(10))
                                            await TempClient(UpdateUsernameRequest(ran))
                                            setted = True
                                        except:
                                            await asyncio.sleep(10)
                                            pass
                                    await e.edit("NUMERO OTTENUTO : " + number,
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])

                                else:
                                    if five_sim_client.ban_number(order["id"]) is True:
                                        await e.edit("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                                     buttons=[[Button.inline("🔙 Indietro", "back")]])
                                    else:
                                        await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                                     buttons=[[Button.inline("🔙 Indietro", "back")]])

                            except FloodWaitError as floderr:
                                await e.edit(f"**⏳ Attendi altri {floderr.seconds} ⏳*per il voip attuale sarà chiesto un rimborso.*", buttons=[[Button.inline("🔙 Indietro", "back")]])
                                if five_sim_client.ban_number(order["id"]) is True:
                                    await e.respond("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                                    buttons=[[Button.inline("🔙 Indietro", "back")]])
                                else:
                                    await e.respond("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                                    buttons=[[Button.inline("🔙 Indietro", "back")]])
                                await asyncio.sleep(floderr.seconds + 4)
                            except Exception as e6:
                                print(e6)

                                if five_sim_client.ban_number(order["id"]) is True:
                                    await e.edit("NUMERO NON FUNZIONANTE, MA RIMBORSO OTTENUTO.",
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])
                                else:
                                    await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, CONTROLLARE CHIAVE API, RATING, E TUTTO DAL VOSTRO ACC. 5SIM.",
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])
                        else:
                            await e.edit("**NUMERO NON TROVATO**",
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"fivesimset":
            Getter = 16
            await e.edit("**INVIA CHIAVE API 5SIM**",
                         buttons=[[Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"onlinesimru":
            if onlinesim_api is None:
                await e.edit("**NESSUNA CHIAVE API **",
                             buttons=[[Button.inline("SET ONLINESIM APIKEY", "onlinesimset")],
                                      [Button.inline("🔙 Indietro", "back")]])
            else:
                await e.edit("sto provando ad ottenere un voip..")
                order = onlinesim_client.Get_order("33", "Telegram")
                if order is not None:
                    number = onlinesim_client.get_number_from_order(
                        order["id"])
                    print(number)
                    try:
                        number = number.strip()
                        TempClient = TMPTelegramClient(
                            StringSession(), API_KEY, API_HASH)
                        await TempClient.connect()
                        await TempClient.send_code_request(number)
                        tentativi = 0
                        Code = None
                        Limitator = True
                        while Limitator:
                            code = onlinesim_client.get_code(order["id"])
                            if code is not None:
                                Code = code
                                Limitator = False
                            else:
                                tentativi = tentativi + 1
                                await asyncio.sleep(10)
                                if tentativi > 46:
                                    Limitator = False

                        if Code is not None:
                            await TempClient.sign_up(str(Code), first_name='ANNINO', last_name='Fragola')
                            SSs[number] = StringSession.save(
                                TempClient.session)
                            await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                            setted = False
                            while not setted:
                                try:
                                    ran = "".join(random.choice(
                                        string.ascii_letters) for i in range(10))
                                    await TempClient(UpdateUsernameRequest(ran))
                                    setted = True
                                except:
                                    await asyncio.sleep(10)
                                    pass

                            saveSS()
                            await e.edit("NUMERO OTTENUTO : " + number,
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])
                        else:
                            await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, ONLINE SIM NON ATTUALMENTE SUPPORTATO PER RIMBORSO (AUTO).\n FARE MANUALMENTE.",
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])

                    except FloodWaitError as floderr:
                        await e.edit(f"**⏳ Attendi altri {floderr.seconds} ⏳*per il voip attuale non sarà chiesto un rimborso.(api)*", buttons=[[Button.inline("🔙 Indietro", "back")]])
                        await asyncio.sleep(floderr.seconds + 4)
                    except Exception as e6:
                        print(e6)
                        await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, ONLINE SIM NON ATTUALMENTE SUPPORTATO PER RIMBORSO (AUTO).\n FARE MANUALMENTE.",
                                     buttons=[[Button.inline("🔙 Indietro", "back")]])
                else:
                    order = onlinesim_client.Get_order("506", "Telegram")
                    if order is not None:
                        number = onlinesim_client.get_number_from_order(
                            order["id"]).strip()
                        try:
                            TempClient = TMPTelegramClient(
                                StringSession(), API_KEY, API_HASH)
                            await TempClient.connect()
                            await TempClient.send_code_request(number)
                            tentativi = 0
                            Code = None
                            Limitator = True
                            while Limitator:
                                code = onlinesim_client.get_code(order["id"])
                                if code is not None:
                                    Code = code
                                    Limitator = False
                                else:
                                    tentativi = tentativi + 1
                                    await asyncio.sleep(10)
                                    if tentativi > 46:
                                        Limitator = False

                            if Code is not None:
                                await TempClient.sign_up(Code, first_name='ANNINO', last_name='Fragola')
                                SSs[number] = StringSession.save(
                                    TempClient.session)
                                await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                                setted = False
                                while not setted:
                                    try:
                                        ran = "".join(random.choice(
                                            string.ascii_letters) for i in range(10))
                                        await TempClient(UpdateUsernameRequest(ran))
                                        setted = True
                                    except:
                                        await asyncio.sleep(10)
                                        pass

                                saveSS()
                                await e.edit("NUMERO OTTENUTO : " + number,
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])
                            else:
                                await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, ONLINE SIM NON ATTUALMENTE SUPPORTATO PER RIMBORSO (AUTO).\n FARE MANUALMENTE.",
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])

                        except FloodWaitError as floderr:
                            await e.edit(f"**⏳ Attendi altri {floderr.seconds} ⏳*per il voip attuale non sarà chiesto un rimborso.(api)*", buttons=[[Button.inline("🔙 Indietro", "back")]])
                            await asyncio.sleep(floderr.seconds + 4)
                        except Exception as e6:
                            print(e6)
                            await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, ONLINE SIM NON ATTUALMENTE SUPPORTATO PER RIMBORSO (AUTO).\n FARE MANUALMENTE.",
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])
                    else:
                        order = onlinesim_client.Get_order("48", "Telegram")
                        if order is not None:
                            number = onlinesim_client.get_number_from_order(
                                order["id"]).strip()
                            try:
                                TempClient = TMPTelegramClient(
                                    StringSession(), API_KEY, API_HASH)
                                await TempClient.connect()
                                await TempClient.send_code_request(number)
                                tentativi = 0
                                Code = None
                                Limitator = True
                                while Limitator:
                                    code = onlinesim_client.get_code(
                                        order["id"])
                                    if code is not None:
                                        Code = code
                                        Limitator = False
                                    else:
                                        tentativi = tentativi + 1
                                        await asyncio.sleep(10)
                                        if tentativi > 46:
                                            Limitator = False
                                if Code is not None:
                                    await TempClient.sign_up(Code, first_name='ANNINO', last_name='Fragola')
                                    SSs[number] = StringSession.save(
                                        TempClient.session)
                                    await TempClient(UploadProfilePhotoRequest(await TempClient.upload_file(path)))
                                    setted = False
                                    while not setted:
                                        try:
                                            ran = "".join(random.choice(
                                                string.ascii_letters) for i in range(10))
                                            await TempClient(UpdateUsernameRequest(ran))
                                            setted = True
                                        except:
                                            await asyncio.sleep(10)
                                            pass

                                    saveSS()
                                    await e.edit("NUMERO OTTENUTO : " + number,
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])
                                else:
                                    await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, ONLINE SIM NON ATTUALMENTE SUPPORTATO PER RIMBORSO (AUTO).\n FARE MANUALMENTE.",
                                                 buttons=[[Button.inline("🔙 Indietro", "back")]])

                            except FloodWaitError as floderr:
                                await e.edit(f"**⏳ Attendi altri {floderr.seconds} ⏳*per il voip attuale non sarà chiesto un rimborso (api).*", buttons=[[Button.inline("🔙 Indietro", "back")]])
                                await asyncio.sleep(floderr.seconds + 4)
                            except Exception as e6:
                                print(e6)
                                await e.edit("NUMERO NON FUNZIONANTE, RIMBORSO NON OTTENUTO, ONLINE SIM NON ATTUALMENTE SUPPORTATO PER RIMBORSO (AUTO).\n FARE MANUALMENTE.",
                                             buttons=[[Button.inline("🔙 Indietro", "back")]])
                        else:
                            await e.edit("NUMERI TERMINATI : ",
                                         buttons=[[Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"onlinesimset":
            Getter = 17
            await e.edit("**INVIA CHIAVE API ONLINESIM.RU**",
                         buttons=[[Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"voip":
            Getter, Number, TempClient = None, None, None
            await e.edit(f"__📞 Voip Aggiunti »__ **{SSs.__len__()}**",
                         buttons=[[Button.inline("➕ Aggiungi", "addvoip"), Button.inline("🔧 Gestisci", "voips")],
                                  [Button.inline("📁 Archiviati", "arch")], [Button.inline("➕➕CREA DA PIATTAFORMA", "makevoip")],  [Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"addvoip":
            Getter = 0
            await e.edit("**☎️ Inserisci il numero del voip che desideri aggiungere ☎️**",
                         buttons=[Button.inline("❌ Annulla", "voip")])
        elif e.data == b"voips":
            if SSs.__len__() > 0:
                Getter = 3
                msg = "__☎️ Invia il numero del voip che vuoi gestire__\n\n**LISTA VOIP**"
                for n in SSs:
                    msg += f"\n`{n}`"
                await e.edit(msg, buttons=[Button.inline("❌ Annulla", "voip")])
            else:
                await e.edit("**❌ Non hai aggiunto nessun voip ❌**",
                             buttons=[[Button.inline("➕ Aggiungi", "addvoip")], [Button.inline("🔙 Indietro", "voip")]])
        elif e.data == b"arch":
            if ArchSSs.__len__() > 0:
                Getter = 4
                msg = f"__📁 Voip Archiviati »__ **{ArchSSs.__len__()}**\n\n__☎️ Invia il numero del voip archiviato che vuoi gestire__\n\n**LISTA VOIP ARCHIVIATI**"
                for n in ArchSSs:
                    msg += f"\n`{n}`"
                await e.edit(msg, buttons=[Button.inline("❌ Annulla", "voip")])
            else:
                await e.edit("**❌ Non hai archiviato nessun voip ❌**", buttons=[[Button.inline("🔙 Indietro", "voip")]])
        elif e.data == b"grab":
            if Grab == None:
                await e.edit("**❌ Gruppo Non Impostato ❌\n\nℹ️ Puoi impostarlo usando il bottone qui sotto!**",
                             buttons=[[Button.inline("✍🏻 Imposta", "setgrab")],
                                      [Button.inline("🔙 Indietro 🔙", "back")]])
            else:
                await e.edit(f"__👥 Gruppo impostato »__ **{Grab}**",
                             buttons=[[Button.inline("✍🏻 Modifica", "setgrab")],
                                      [Button.inline("🔙 Indietro", "back")]])
        elif e.data == b"setgrab":
            Getter = 5
            await e.edit("__👥 Invia la @ o il link del gruppo da cui vuoi rubare gli utenti!__",
                         buttons=[Button.inline("❌ Annulla", "back")])
        elif e.data == b"changedevice":
            actualdevice = random.choice(devices)  # Seleziona un nuovo dispositivo
            save_device(actualdevice)  # Salva immediatamente il nuovo dispositivo

    # Verifica del dispositivo selezionato
            print(f"Dispositivo selezionato: {actualdevice['m_name']}")
    
    # Risposta al comando con il dispositivo selezionato
            await e.answer(
        f"Dispositivo cambiato!\n\nDispositivo: {actualdevice['m_name']}\nVersione sistema: {actualdevice['s_name']}\nVersione Telegram: {actualdevice['s_app']}",
        alert=True
        )
        elif e.data == b"add":
            if SSs.__len__() > 0:
                if Grab != None:
                    Getter = 6
                    await e.edit("__➕ Invia la @ o il link del gruppo in cui vuoi aggiungere gli utenti!__",
                                buttons=[[Button.inline("❌ Annulla", "back")]])
                else:
                    await e.edit("**❌ Impostare il gruppo da cui rubare gli utenti ❌**",
                                 buttons=[[Button.inline("👥 Ruba", "grab")], [Button.inline("🔙 Indietro", "back")]])
            else:
                await e.edit("**❌ Non hai aggiunto nessun voip ❌**",
                             buttons=[[Button.inline("➕ Aggiungi", "addvoip")], [Button.inline("🔙 Indietro", "back")]])
        else:
            st = e.data.decode().split(";")
            if st[0] == "setnome":
                if st[1] in SSs:
                    Getter = 12
                    TempClient = TMPTelegramClient(
                        StringSession(SSs[st[1]]), API_KEY, API_HASH)
                    await TempClient.connect()
                    me = await TempClient.get_me()
                    await e.edit("**inserisci il nome da inserire per l'account**\nnome attuale: " + me.first_name)
            elif st[0] == "setcognome":
                if st[1] in SSs:
                    Getter = 13
                    TempClient = TMPTelegramClient(
                        StringSession(SSs[st[1]]), API_KEY, API_HASH)
                    await TempClient.connect()
                    me = await TempClient.get_me()
                    await e.edit(
                        "**inserisci il cognome da inserire per l'account**\ncognome attuale: " + str(me.last_name))
            elif st[0] == "getmsg":
                TempClient = TMPTelegramClient(
                    StringSession(SSs[st[1]]), API_KEY, API_HASH)
                await TempClient.connect()
                messages = await TempClient.get_messages(777000, limit=1)
                await e.client.send_message(e.sender_id, "il tuo messaggio di accesso per il voip è:\n\n" + messages[0].message)
            elif st[0] == "setta":
                if st[1] in SSs:
                    await e.edit(
                        "🔧IMPOSTAZIONI VOIP🔧 : " +
                        st[1] + "\nUsa /start per tornare indietro\n\nscegli cosa fare:",
                        buttons=[
                            [Button.inline("🔶OTTIENI MESSAGGIO🔶", "getmsg;" + st[1])], [
                                Button.inline("🔸SETTA USERNAME🔸", "setusername;" + st[1])],
                            [Button.inline("🔹SETTA FOTO PROFILO🔹",
                                           "setphoto;" + st[1])],
                            [Button.inline(
                                "🔶SETTA NOME🔶", "setnome;" + st[1])],

                            [Button.inline("🔷SETTA COGNOME🔷", "setcognome;" + st[1])]])
            elif st[0] == "visualizza":
                if st[1] in SSs:
                    try:
                        TempClient = TMPTelegramClient(
                            StringSession(SSs[st[1]]), API_KEY, API_HASH)
                        await TempClient.connect()
                        me = await TempClient.get_me()
                        cognome = ["𝕊𝕌𝕏ℝ𝕆𝔹_𝔻𝕆𝔹ℝ𝕀𝕐", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "𝔸𝕡𝕠𝕔𝕒𝕝𝕪𝕡𝕤𝕖_𝕀𝕡𝕥𝕧", "» 𝐛𝐞𝐫𝐭! ✰",
    "🆂🅷🆄🅷🆁🅰️🆃 ∅", "𝐊𝐢𝐝𝐝𝐲 🧑‍💻", "☪︎⋆ ᎡᏆᏟᏦᎽ ᏚᎻᏫᏢ ☪︎⋆", "4𝐌𝐒1𝐗 "]
                        
                        if me.last_name == None:
                            await TempClient(UpdateProfileRequest(last_name=random.choice(cognome)))
                        await bot.send_message(e.sender_id,
                                               "\nnome :" + str(me.first_name) + "\ncognome: " +
                                               me.last_name + "\nid: " + str(
                                                   me.id) + " Visualizza: https://t.me/" + me.username + "\nUSA /start per tornare indietro",
                                               buttons=[[Button.inline("🔧IMPOSTAZIONI VOIP🔧", "setta;" + st[1])]])

                    except:
                        TempClient = TMPTelegramClient(
                            StringSession(SSs[st[1]]), API_KEY, API_HASH)
                        await TempClient.connect()
                        me = await TempClient.get_me()
                        cognome = ["𝕊𝕌𝕏ℝ𝕆𝔹_𝔻𝕆𝔹ℝ𝕀𝕐", "₳₦₲ɆⱠØ ᴰᵉᵛᵉˡᵒᵖᵉʳ", "𝔸𝕡𝕠𝕔𝕒𝕝𝕪𝕡𝕤𝕖_𝕀𝕡𝕥𝕧", "» 𝐛𝐞𝐫𝐭! ✰",
    "🆂🅷🆄🅷🆁🅰️🆃 ∅", "𝐊𝐢𝐝𝐝𝐲 🧑‍💻", "☪︎⋆ ᎡᏆᏟᏦᎽ ᏚᎻᏫᏢ ☪︎⋆", "4𝐌𝐒1𝐗 "]
                        if me.last_name == None:
                            await TempClient(UpdateProfileRequest(last_name=random.choice(cognome)))
                        
                        if me.username == None:

                            await TempClient(UpdateUsernameRequest("Magia_"+str(me.id)))
                        await bot.send_message(e.sender_id,
                                               "\nnome :" + me.first_name + "\ncognome: " +
                                               me.last_name + "\nid: " + str(
                                                   me.id) + " Visualizza: https://t.me/" + me.username + "\nUSA /start per tornare indietro",
                                               buttons=[[Button.inline("🔧IMPOSTAZIONI VOIP🔧", "setta;" + st[1])]])

            elif st[0] == "setusername":
                if st[1] in SSs:
                    Getter = 9
                    TempClient = TMPTelegramClient(
                        StringSession(SSs[st[1]]), API_KEY, API_HASH)
                    await TempClient.connect()
                    me = await TempClient.get_me()
                    await e.edit("**inserisci l'username da inserire per l'account**\nusername attuale: " + str(me.username),
                                 buttons=[[Button.inline("🔙 Indietro", "back")]])
            elif st[0] == "setphoto":
                if st[1] in SSs:
                    Getter = 10
                    TempClient = TMPTelegramClient(
                        StringSession(SSs[st[1]]), API_KEY, API_HASH)
                    await TempClient.connect()
                    await e.edit("**invia la foto da inserire per l'account**",
                                 buttons=[[Button.inline("🔙 Indietro", "voip")]])
            elif st[0] == "arch":
                if st[1] in SSs:
                    if not st[1] in ArchSSs:
                        ArchSSs[st[1]] = SSs[st[1]]
                        saveArchSS()
                    del (SSs[st[1]])
                    saveSS()
                    await e.edit("**✅ Voip Archiviato Correttamente ✅**",
                                 buttons=[[Button.inline("🔙 Indietro", "voip")]])
                else:
                    await e.edit("**❌ Voip Non Trovato ❌**", buttons=[[Button.inline("🔙 Indietro", "voip")]])

            elif st[0] == "add":
                if st[1] in ArchSSs:
                    SSs[st[1]] = ArchSSs[st[1]]
                    saveSS()
                    del (ArchSSs[st[1]])
                    saveArchSS()
                    await e.edit("**✅ Voip Riaggiunto Correttamente ✅**",
                                 buttons=[[Button.inline("🔙 Indietro", "voip")]])
                else:
                    await e.edit("**❌ Voip Non Trovato ❌**", buttons=[[Button.inline("🔙 Indietro", "voip")]])
            elif st[0] == "del":
                if st[1] in SSs:
                    try:
                        CClient = TMPTelegramClient(
                            StringSession(SSs[st[1]]), API_KEY, API_HASH)
                        await CClient.connect()
                        me = await CClient.get_me()
                        if me != None:
                            async with CClient as client:
                                await client.log_out()
                    except:
                        pass
                    del (SSs[st[1]])
                    saveSS()
                    await e.edit("**✅ Voip Rimosso Correttamente ✅**", buttons=[[Button.inline("🔙 Indietro", "voip")]])
                else:
                    await e.edit("**❌ Voip Già Rimosso ❌**", buttons=[[Button.inline("🔙 Indietro", "voip")]])
            elif st[0] == "delarch":
                if st[1] in ArchSSs:
                    try:
                        CClient = TMPTelegramClient(
                            StringSession(SSs[st[1]]), API_KEY, API_HASH)
                        await CClient.connect()
                        me = await CClient.get_me()
                        if me != None:
                            async with CClient as client:
                                await client.log_out()
                    except:
                        pass
                    del (ArchSSs[st[1]])
                    saveArchSS()
                    await e.edit("**✅ Voip Rimosso Correttamente ✅**", buttons=[[Button.inline("🔙 Indietro", "voip")]])
                else:
                    await e.edit("**❌ Voip Già Rimosso ❌**", buttons=[[Button.inline("🔙 Indietro", "voip")]])
            elif st[0] == "info":
                await e.answer(f"ℹ️ L' errore è avvenuto nel seguente voip » {st[1]} ℹ️")

print("mi raccomando, inserisci il token del bot..")
bot.start()







bot.run_until_disconnected()
