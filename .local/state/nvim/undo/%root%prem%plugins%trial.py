Vim�UnDo� ��֠-�A<�r�{��A;�z��=�� ���~��   M           return   0                          d��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             d��l     �                   �               5��                    �                      �@      5�_�                    2        ����                                                                                                                                                                                                                                                                                                                            �           2           v        d��~     �   1   3  �   d   j = None   w = None   proto = None   "@Client.on_callback_query(group=2)   (async def renew(client, callback_query):       global j       global w       global proto   (    if "rlinode" == callback_query.data:           keyboard = []   B        j = Rnew("biznet.madewgn.eu.org", "potatoNTfciWgX4g2zF2c")   '        for option in options['renew']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)           &    elif "rdo" == callback_query.data:           keyboard = []   8        j = Rnew("do.madewgn.eu.org", "SCPotato933028=")   '        for option in options['renew']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)   (    elif "rnusa" == callback_query.data:           keyboard = []   @        j = Rnew("nusa.madewgn.eu.org", "potato98omenbDX4hdnLa")   '        for option in options['renew']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)               *    elif "rrajasa" == callback_query.data:           keyboard = []   1        j = Rnew("wijaya.madewgn.eu.org", wijaya)   '        for option in options['renew']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)               =    elif callback_query.data in ["vmess", "vless", "trojan"]:           if j is not None:               wak = w               server = j   '            proto = callback_query.data               keyboard = []   *            for option in options['hari']:   7                button_text = remove_underscore(option)   Z                keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   9            reply_markup = InlineKeyboardMarkup(keyboard)   _            await callback_query.message.reply_text('Choose renew:', reply_markup=reply_markup)                   else:               print("j is None")              %    elif "30" in callback_query.data:           server = j           waktu = w           proto = proto   g        i = await callback_query.message.chat.ask('**username:**', parse_mode=enums.ParseMode.MARKDOWN)           h = i.text.lower()   E        await i.request.edit_text(f"bentar ya!\nusername: {i.text} ")   6        chat_id = str(callback_query.message.chat.id)    '        if hasattr(server, str(proto)):   .            func = getattr(server, str(proto))   !            x = await func(h, 30)   0            await callback_query.message.edit(x)   $            await i.request.delete()               harga = 5   #            db.beli(chat_id, harga)       %    elif "60" in callback_query.data:           server = j           waktu = w           proto = proto   g        i = await callback_query.message.chat.ask('**username:**', parse_mode=enums.ParseMode.MARKDOWN)           h = i.text.lower()   E        await i.request.edit_text(f"bentar ya!\nusername: {i.text} ")   6        chat_id = str(callback_query.message.chat.id)    '        if hasattr(server, str(proto)):   .            func = getattr(server, str(proto))   !            x = await func(h, 60)               harga = 4 * 2   0            await callback_query.message.edit(x)   $            await i.request.delete()   #            db.beli(chat_id, harga)               def remove_underscore(string):5��    1       c               �      �              5�_�                    <        ����                                                                                                                                                                                                                                                                                                                            <           �           v���    d���    �   ;   =  A   �   #s = None  # Define a global variabl       
isp = None   "@Client.on_callback_query(group=1)   'async def prem(client, callback_query):       global s       global isp       '    if "biznet" == callback_query.data:   -        await callback_query.message.delete()           isp = "Biznet"           keyboard = []   F        s = BuatAkun("biznet.madewgn.eu.org", "potatoNTfciWgX4g2zF2c")   %        for option in options['biz']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)       '    if "linode" == callback_query.data:   -        await callback_query.message.delete()           isp = "Linode"           keyboard = []   F        s = BuatAkun("linode.madewgn.eu.org", "potatoR2P9sThDSGKjA9b")   %        for option in options["ssh"]:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)               %    elif "do" == callback_query.data:   -        await callback_query.message.delete()           isp = "Digital Ocean"           keyboard = []   C        s = BuatAkun("aws.madewgn.eu.org", "potatofBDd44R0fNZd9wM")   &        for option in options['xray']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)       &    elif "idc" == callback_query.data:   -        await callback_query.message.delete()           isp = "idc"           keyboard = []   0        s = Buat("id.madewgn.eu.org", "madewgn")   (        for option in options['server']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)           '    elif "nusa" == callback_query.data:   -        await callback_query.message.delete()           isp = "Nusa"           keyboard = []   D        s = BuatAkun("nusa.madewgn.eu.org", "potato98omenbDX4hdnLa")   &        for option in options['xray']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)       )    elif "rajasa" == callback_query.data:   -        await callback_query.message.delete()           isp = "Wijaya"           keyboard = []   5        s = BuatAkun("wijaya.madewgn.eu.org", wijaya)   (        for option in options['server']:   3            button_text = remove_underscore(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   `        await callback_query.message.reply_text('Choose a protocol:', reply_markup=reply_markup)               q    elif callback_query.data in ["trojan_ws", "trojan_grpc", "vmess_ws", "vmess_grpc", "vless_ws", "vless_grpc"]:           if s is not None:               if isp == "idc":                   server = s                       else:                   server = s       o                i = await callback_query.message.chat.ask('**username:**', parse_mode=enums.ParseMode.MARKDOWN)   w                hari = await callback_query.message.chat.ask('**expride (day):**', parse_mode=enums.ParseMode.MARKDOWN)       "                h = i.text.lower()   M                await i.request.edit_text(f"bentar ya!\nusername: {i.text} ")   =                chat_id = str(callback_query.message.chat.id)   0                cekk = db.ceksaldo(str(chat_id))   +                xx = int(hari.text) * harga   '                if int(cekk) < int(xx):   #                    print("kurang")   [                    await client.send_message(chat_id=int(chat_id),text=f"Saldo mu kurang")                   else:                          <                    if hasattr(server, callback_query.data):   C                        func = getattr(server, callback_query.data)   9                        x = await func(h, int(hari.text))   <                        await callback_query.message.edit(x)   0                        await i.request.delete()   ,                        db.beli(chat_id, xx)   8                        cekk = db.ceksaldo(str(chat_id))   G                        #                        tran = db.transaksi(1)   %#                         texx = f"""   5# **⚡️ Transaksi Portal Ke. {tran["transaksi"]}**   5# ━━━━━━━━━━━━━━━━━   R#  Transaksi : Akun **{remove_underscore(callback_query.data)}** {hari.text} Hari    #  Server : **{isp}**   5# ━━━━━━━━━━━━━━━━━   7# Notifikasi Otomatis Via Panel                           #                         """   g                        await client.send_message(chat_id=int(chat_id),text=f"sisa saldo mu Rp.{cekk}")   n                        #                        await client.send_message(chat_id="-1001917126110",text=texx)                                   else:   u                        await callback_query.message.reply_text(f"Attribute {callback_query.data} is not supported.")           else:               print("s is None")               '    elif "SSH" == callback_query.data :           if s is not None:               if isp == "idc":                   p = "p"               else:   =                chat_id = str(callback_query.message.chat.id)                   print(chat_id)                   server = s   o                i = await callback_query.message.chat.ask('**username:**', parse_mode=enums.ParseMode.MARKDOWN)   p                pw = await callback_query.message.chat.ask('**password:**', parse_mode=enums.ParseMode.MARKDOWN)   w                hari = await callback_query.message.chat.ask('**expride (day):**', parse_mode=enums.ParseMode.MARKDOWN)       _                await callback_query.message.edit(f"bentar ya!\nuser: {i.text}\npw: {pw.text}")   0                cekk = db.ceksaldo(str(chat_id))   +                xx = int(hari.text) * harga   '                if int(cekk) < int(xx):   #                    print("kurang")   b                    await client.send_message(chat_id=int(chat_id),text=f"Saldo mu kurang")          O        #         await i.request.edit_text(f"bentar ya!\nusername: {i.text} ")                   else:   <                    if hasattr(server, callback_query.data):   C                        func = getattr(server, callback_query.data)   A                        x = await func(i.text,pw.text, hari.text)   <                        await callback_query.message.edit(x)   0                        await i.request.delete()   ,                        db.beli(chat_id, xx)   0#                         tran = db.transaksi(1)   %#                         texx = f"""   5# **⚡️ Transaksi Portal Ke. {tran["transaksi"]}**   5# ━━━━━━━━━━━━━━━━━   R#  Transaksi : Akun **{remove_underscore(callback_query.data)}** {hari.text} Hari    #  Server : **{isp}**   5# ━━━━━━━━━━━━━━━━━   7# Notifikasi Otomatis Via Panel                           #                         """   #   g                        await client.send_message(chat_id=int(chat_id),text=f"sisa saldo mu Rp.{cekk}")   W#                         await client.send_message(chat_id="-1001917126110",text=texx)                               else:   u                        await callback_query.message.reply_text(f"Attribute {callback_query.data} is not supported.")           else:               print("s is None")        5��    ;       �               I      e              5�_�                    /        ����                                                                                                                                                                                                                                                                                                                            <           <           v���    d���     �   .   I   �       �   /   0   �    5��    .                      �              �      5�_�                    /       ����                                                                                                                                                                                                                                                                                                                            U           U           v���    d���     �   .   0   �      opsi = {5��    .                     �                    5�_�                    /       ����                                                                                                                                                                                                                                                                                                                            U           U           v���    d���    �   .   0   �      list = {5��    .                     �                    5�_�                            ����                                                                                                                                                                                                                                                                                                                                       �           v        d���    �                   �               �               �   from os import wait   from . import id   from pyrogram import *   from pyrogram.types import (       InlineKeyboardMarkup,       InlineKeyboardButton,       CallbackQuery,       Message   )   import pyromod   from . import db   from .will import Buat, Tria   &from .ssg import BuatAkun, Rnew, Trial       	def su():       sudo = db.getall()   !    return [int(x) for x in sudo]       sudo_int = su()       cmd = ""       harga = 167   sid = "ID RAJASA"   ssg = "SG LINODE"       ;linode = BuatAkun("aws.madewgn.eu.org", "XyXMadeSCPotato=")   ?rajasa = BuatAkun("rajasa.madewgn.eu.org", "PotatoUbuntu2905=")        wijaya = "potatobE93LmhUrjq1S7c"       options = {   f    'server':  ["SSH","trojan_ws", "trojan_grpc", "vmess_ws", "vmess_grpc", "vless_ws", "vless_grpc"],   ^    'xray':  ["trojan_ws", "trojan_grpc", "vmess_ws", "vmess_grpc", "vless_ws", "vless_grpc"],       'ssh': ["SSH"],       'tssh': ["tSSH"],       'biz': ["SSH","vmess_ws"],   !    'tbiz': ["tSSH","tvmess_ws"],   e    'txray':  ["ttrojan_ws", "ttrojan_grpc", "tvmess_ws", "tvmess_grpc", "tvless_ws", "tvless_grpc"],   l    'trial':  ["tSSH","ttrojan_ws", "ttrojan_grpc", "tvmess_ws", "tvmess_grpc", "tvless_ws", "tvless_grpc"],   )    'renew': ['trojan', 'vmess',"vless"],       'hari': ['30', '60']   }               l = {   B    "server": ["SG DO","SG LINODE","ID NUSA","ID BIZNET","ID IKD"]   }           def ambil_teks(input_teks):   .    # Mengambil teks setelah dua huruf pertama   +    teks_setelah_dua_huruf = input_teks[2:]          "    # Mengambil teks setelah spasi   @    teks_setelah_spasi = teks_setelah_dua_huruf.split(' ', 1)[1]          %    return teks_setelah_spasi.strip()           def ambil_trial(input_teks):   .    # Mengambil teks setelah dua huruf pertama   +    teks_setelah_dua_huruf = input_teks[2:]          "    # Mengambil teks setelah spasi   @    teks_setelah_spasi = teks_setelah_dua_huruf.split(' ', 1)[1]          &    x = "t"+teks_setelah_spasi.strip()       return x.lower()                   def remove_underscore(string):        x = string.replace("_", " ")       return x.upper()                   def remove_trial(string):   7    return string.replace("_", " ").replace("t", "", 1)           "@Client.on_callback_query(group=3)   )async def triall(client, callback_query):       global s       (    if "tbiznet" == callback_query.data:   .        #await callback_query.message.delete()           keyboard = []   C        s = Trial("biznet.madewgn.eu.org", "potatoNTfciWgX4g2zF2c")   &        for option in options['tbiz']:   .            button_text = remove_trial(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   Z        await callback_query.message.edit('Choose a protocol:', reply_markup=reply_markup)           &    elif "tdo" == callback_query.data:   .#        await callback_query.message.delete()           keyboard = []   @        s = Trial("aws.madewgn.eu.org", "potatofBDd44R0fNZd9wM")   '        for option in options['txray']:   .            button_text = remove_trial(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   Z        await callback_query.message.edit('Choose a protocol:', reply_markup=reply_markup)   (    if "tlinode" == callback_query.data:   .        #await callback_query.message.delete()           keyboard = []   C        s = Trial("linode.madewgn.eu.org", "potatoR2P9sThDSGKjA9b")   &        for option in options['tssh']:   .            button_text = remove_trial(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   Z        await callback_query.message.edit('Choose a protocol:', reply_markup=reply_markup)           (    elif "tnusa" == callback_query.data:   .#        await callback_query.message.delete()           keyboard = []   A        s = Trial("nusa.madewgn.eu.org", "potato98omenbDX4hdnLa")   '        for option in options['txray']:   .            button_text = remove_trial(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   Z        await callback_query.message.edit('Choose a protocol:', reply_markup=reply_markup)       '    elif "tikd" == callback_query.data:   .#        await callback_query.message.delete()               keyboard = []   /        s = Trial("ikd.madewgn.eu.org", wijaya)   '        for option in options['trial']:   .            button_text = remove_trial(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   Z        await callback_query.message.edit('Choose a protocol:', reply_markup=reply_markup)               '    elif "tidc" == callback_query.data:   .#        await callback_query.message.delete()           keyboard = []   0        s = Tria("id.madewgn.eu.org", "madewgn")       '        for option in options['trial']:   .            button_text = remove_trial(option)   V            keyboard.append([InlineKeyboardButton(button_text, callback_data=option)])   5        reply_markup = InlineKeyboardMarkup(keyboard)   Z        await callback_query.message.edit('Choose a protocol:', reply_markup=reply_markup)           ~    elif callback_query.data in ["tSSH","ttrojan_ws", "ttrojan_grpc", "tvmess_ws", "tvmess_grpc", "tvless_ws", "tvless_grpc"]:           if s is not None:   !            server = s              4            if hasattr(server, callback_query.data):   ;                func = getattr(server, callback_query.data)                    x = await func()   ;                return await callback_query.message.edit(x)                       else:   m                await callback_query.message.reply_text(f"Attribute {callback_query.data} is not supported.")           else:               print("s is None")                5��            �                       �              �                    J                       �
      5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                  v        d���    �      	   K       5��                          �                      �                         �                      �                         �                      �       
                  �                      �       	                  �                      �                         �                      �                         �                      �                     
   �              
       �                         �                      �                         �                      �                         �                      �                        �                     �                         �                      �                        �                     �                         �                      �                         �                      �                        �                     �                        �                     �                        �                     5�_�      
           	   *        ����                                                                                                                                                                                                                                                                                                                                                  v        d��    �   )   +   K       5��    )                      �                     �    )                    �                    5�_�   	              
   :   1    ����                                                                                                                                                                                                                                                                                                                                                             d�ŕ     �   9   ;   K      3        for option in options[callback_query.data]:5��    9                     t                     5�_�   
                 :       ����                                                                                                                                                                                                                                                                                                                                                             d�Ř     �   9   ;   K               for option in options[]:5��    9                     t                     5�_�                    :       ����                                                                                                                                                                                                                                                                                                                                                             d�ř   	 �   9   ;   K      "        for option in options[""]:5��    9                     u                     �    9                    t                    �    9                    t                    �    9                    t                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��V   
 �      	   K      )5��                         �                      �                          �                      �                         �                      �                         �                     5�_�                    /        ����                                                                                                                                                                                                                                                                                                                                                             d��     �   .   0   L       �   /   0   L    5��    .                   I                 I       5�_�                    /        ����                                                                                                                                                                                                                                                                                                                                                             d��     �   .   0   L      Iif callback_query.message is None or callback_query.message.chat is None:5��    .                                           5�_�                    0       ����                                                                                                                                                                                                                                                                                                                                                             d��    �   /   1   L      M    if callback_query.data in ["tbiznet", "tdo", "tlinode", "tnusa", "tikd"]:5��    /                     Y                     5�_�                     /   M    ����                                                                                                                                                                                                                                                                                                                                                             d��    �   /   1   M              return�   .   1   L      M    if callback_query.message is None or callback_query.message.chat is None:5��    .   M                 T                     �    /                     Y                     �    /   
                  _                     �    /   	                  ^                     �    /                    ]                    �    /                    ]                    �    /                    ]                    5��