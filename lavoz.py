#Importamos la clase Bot de instabot para poder instanciarlo y usarlo.
from instabot import Bot
#shutil y OS para poder eliminar la carpeta config que crea instabot.
import shutil
import os
#Datetime para poder elegir el archivo del dia.
from datetime import datetime

hoy = datetime.today().strftime('%d-%m-%Y')
imagen = hoy + '.jpg'
dir_to_delete = 'config'

#os.mkdir('config')

if len(os.listdir(dir_to_delete)) == 0:
    print("Directorio config no existe. Es seguro continuar :)")
    #os.rmdir(dir_to_delete)
else:
    print(f"{dir_to_delete} Existe.. Voy a borrar ahora :)")
    shutil.rmtree(dir_to_delete)

#Hashtags
hashtags = "#lavozinterior #eileencaddy #amor #reflexiones #diario #espiritualidad #interior #universo #junio"

#Instacia del bot
bot=Bot()
bot.login(username="**",password="**!")
bot.upload_photo(imagen,caption=hashtags)
