import discord
import time
from selenium import webdriver
from discord.ext import commands, tasks

refresher = webdriver.Chrome('/Users/admin/Desktop/Gabriel Stefanecs Folder/chromedriver')

# refresher = webdriver.Chrome('/Users/stefa/Documents/chromedriver_win32/chromedriver')

refresher.get("https://webinterface.nitrado.net/8944851/wi/gameserver/")

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    taskFunction.start()
    print("Bot is ready")

@tasks.loop(seconds = 1)
async def taskFunction():
    # For using Chrome

    try:

        try:
            main_page = refresher.current_window_handle

            cookieClicker = addButton = refresher.find_element_by_class_name("cb_button-dark")
            cookieClicker.click()

            loginMenu = addButton = refresher.find_element_by_class_name("ni_user-dropdown")
            loginMenu.click()

            time.sleep(5)

            # changing the handles to access login page
            for handle in refresher.window_handles:
                if handle != main_page:
                    login_page = handle

            # change the control to signin page        
            refresher.switch_to.window(login_page)

            username = refresher.find_element_by_id('username')
            username.send_keys("REDACTED")

            password = refresher.find_element_by_id('password')
            password.send_keys("REDACTED")

            time.sleep(5)

            submitButton = refresher.find_element_by_class_name("mb-3")
            submitButton.click()

            time.sleep(6)

            # change control to main page
            refresher.switch_to.window(main_page)

            accountMenu = addButton = refresher.find_element_by_class_name("ni_user-dropdown")
            accountMenu.click()

            myServices = addButton = refresher.find_element_by_xpath("//*[@id=\"__layout\"]/div/nav/div[2]/div[4]/div[2]/div/div/ul/li[4]/a")
            myServices.click()

            gameServer = addButton = refresher.find_element_by_css_selector('[href="/usa/services/index#gameserver"]')
            gameServer.click()

            settings = addButton = refresher.find_element_by_class_name("pull-right")
            settings.click()

            time.sleep(10)

            refresher.switch_to.window(refresher.window_handles[1])

            #refreshBool = False

            #while not refreshBool:

            # Red Circle \U0001F534
            # Green Circle \U0001F7E2
            # Arrows Counterclockwise \U0001F504

            status = refresher.find_element_by_id('game-header')

            online = "Server started"

            offline = "Server stopped"

            stopping = "Stopping server..."

            restarting = "Restarting..."

            if offline in status.text:

                channel = client.get_channel(853748740224712754)
                embed = discord.Embed(title="Server Status", description = ":red_circle: Offline", color = 0xe74c3c)
                message = await channel.send(embed = embed)
                await message.add_reaction('\U0001F7E2')
                await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Offline"))

            elif online in status.text:

                channel = client.get_channel(853748740224712754)
                embed = discord.Embed(title="Server Status", description = ":green_circle: Online", color = 0x2ecc71)
                message = await channel.send(embed = embed)
                await message.add_reaction('\U0001F534')
                await message.add_reaction('\U0001F504')
                await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Online"))

            elif stopping in status.text:

                channel = client.get_channel(853748740224712754)
                embed = discord.Embed(title="Server Status", description = ":octagonal_sign: Stopping...", color = 0xe67e22)
                message = await channel.send(embed = embed)
                await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Stopping"))

            elif restarting in status.text:

                channel = client.get_channel(853748740224712754)
                embed = discord.Embed(title="Server Status", description = ":arrows_counterclockwise: Restarting...", color = 0xf1c40f)
                message = await channel.send(embed = embed)
                await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Restarting"))
    
            else:

                channel = client.get_channel(853748740224712754)
                embed = discord.Embed(title="Server Status", description = ":grey_question: Unknown", color = 0x979c9f)
                message = await channel.send(embed = embed)

        except:

            time.sleep(10)

            channel = client.get_channel(853748740224712754)

            await channel.purge(limit = 1000)

            status = refresher.find_element_by_id('game-header')

            online = "Server started"

            offline = "Server stopped"

            stopping = "Stopping server..."

            restarting = "Restarting..."

            if offline in status.text:

                embed = discord.Embed(title="Server Status", description = ":red_circle: Offline", color = 0xe74c3c)
                message = await channel.send(embed = embed)
                await message.add_reaction('\U0001F7E2')
                await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Offline"))

            elif online in status.text:

                embed = discord.Embed(title="Server Status", description = ":green_circle: Online", color = 0x2ecc71)
                message = await channel.send(embed = embed)
                await message.add_reaction('\U0001F534')
                await message.add_reaction('\U0001F504')
                await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Online"))

            elif stopping in status.text:

                embed = discord.Embed(title="Server Status", description = ":octagonal_sign: Stopping...", color = 0xe67e22)
                message = await channel.send(embed = embed)
                await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Stopping"))

            elif restarting in status.text:

                embed = discord.Embed(title="Server Status", description = ":arrows_counterclockwise: Restarting...", color = 0xf1c40f)
                message = await channel.send(embed = embed)
                await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Restarting"))
    
            else:

                embed = discord.Embed(title="Server Status", description = ":grey_question: Unknown", color = 0x979c9f)
                message = await channel.send(embed = embed)
                await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = "Server: Unknown"))

    except:

        refresher.get("https://webinterface.nitrado.net/8944851/wi/gameserver/")

# Command Code

@client.command()
async def on(ctx):
    taskFunction.stop()

    try:

        status = refresher.find_element_by_id('game-header')

        offline = "Server stopped"

        if offline in status.text:

            await ctx.send("Turning On Server.")

            startServer = addButton = refresher.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[3]')
            startServer.click()

            time.sleep(3)

            startServerConfirm = addButton = refresher.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
            startServerConfirm.click()

        else:

            await ctx.send("You can only turn on the server when it is offline.")

            time.sleep(1)

        taskFunction.restart()

    except:

        await channel.send("An error has occurred, please try again.")

    taskFunction.restart()

@client.command()
async def off(ctx):
    taskFunction.stop()

    try:

        status = refresher.find_element_by_id('game-header')

        online = "Server started"

        if online in status.text:

            await ctx.send("Turning Off Server.")

            stopServer = addButton = refresher.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[1]')
            stopServer.click()

            time.sleep(3)

            stopServerConfirm = addButton = refresher.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
            stopServerConfirm.click()

            taskFunction.restart()

        else:

            await ctx.send("You can only turn off the server when it is online.")

            time.sleep(1)

        taskFunction.restart()

    except:

        await channel.send("An error has occurred, please try again.")

    taskFunction.restart()

@client.command()
async def restart(ctx):

    taskFunction.stop()

    try:

        status = refresher.find_element_by_id('game-header')

        online = "Server started"

        if online in status.text:

            await ctx.send("Restarting Server.")

            restartServer = addButton = refresher.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[2]')
            restartServer.click()

            time.sleep(3)

            restartServerConfirm = addButton = refresher.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
            restartServerConfirm.click()

            taskFunction.restart()

        else:

            await ctx.send("You can only restart the server when it is online.")

            time.sleep(1)

        taskFunction.restart()

    except:

        await channel.send("An error has occurred, please try again.")

    taskFunction.restart()

# Emoji Code

@client.event
async def on_reaction_add(reaction, user):

    try:

        if user == client.user:
            return

        taskFunction.stop()

        status = refresher.find_element_by_id('game-header')

        offline = "Server stopped"

        online = "Server started"

        channel = client.get_channel(853748740224712754)

        if reaction.emoji == '\U0001F7E2':

            if offline in status.text:

                await channel.send("Turning On Server.")

                startServer = addButton = refresher.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[3]')
                startServer.click()

                time.sleep(3)

                startServerConfirm = addButton = refresher.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
                startServerConfirm.click()

                time.sleep(1)

            else:

                await channel.send("Don't do that.:angry:")

                time.sleep(1)

        elif reaction.emoji == '\U0001F534':

            if online in status.text:

                await channel.send("Turning Off Server.")

                startServer = addButton = refresher.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[1]')
                startServer.click()

                time.sleep(3)

                startServerConfirm = addButton = refresher.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
                startServerConfirm.click()

                time.sleep(1)
            
            else:

                await channel.send("Don't do that.:angry:")

                time.sleep(1)

        elif reaction.emoji == '\U0001F504':

            if online in status.text:

                await channel.send("Restarting Server.")

                restartServer = addButton = refresher.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[2]')
                restartServer.click()

                time.sleep(3)

                restartServerConfirm = addButton = refresher.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]')
                restartServerConfirm.click()

                time.sleep(1)

            else:

                await channel.send("Don't do the that.:angry:")

                time.sleep(1)

        else:

            await channel.send("Don't do the that.:angry:")

            time.sleep(1)

    except:

        await channel.send("An error has occurred, please try again.")

    taskFunction.restart()

client.run("REDACTED")



