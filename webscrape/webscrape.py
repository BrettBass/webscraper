import redbot.core
import discord
import pdfkit as pdf


class webScrape(commands.Cog):
        __author__=["Diddly", "Wtitsaduck"]
        __version__=[1.0]
    @commands.command(usage=["<URL>"])
    async def webscrape(self, ctx, url):
    # where bot saves the file(probably gonna be running in linux, so we'll use linux temp directory)
    save-directory = "/tmp/"

    pdf-name = "website.pdf"
    chegg-login = 'https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F'

    pdf.from_url(url, 'website.pdf', configuration=config)
    await ctx.send(file=discord.File("directory" + "pdf-name"))
