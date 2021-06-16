import redbot.core
import discord
import pdfkit as pdf
from sys import platform
import os


class webscrape(commands.Cog):
        __author__=["Diddly", "Wtitsaduck"]
        __version__=[1.0]
    @commands.command(usage=["<URL>"])
    async def webscrape(self, ctx, url):
    # where bot saves the file
    if platform == "linux":
        save-directory = "/tmp/"
    elif platform == "win32"
        running-user = os.getlogin()
        save-directory = f"C:\\Users\\{running-user}\\Appdata\\Local\\Temp\\"

    pdf-name = "website.pdf"
    chegg-login = 'https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F'

    pdf.from_url(url, 'website.pdf', configuration=config)
    await ctx.send(file=discord.File("directory" + "pdf-name"))
