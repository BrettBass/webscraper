import redbot.core
import discord
import pdfkit as pdf


class webScrape(commands.Cog):
        __author__=["Diddly", "Wtitsaduck"]
        __version__=[1.0]
    @commands.command()
    async def webscrape(self, ctx, url):
    #where bot saves the file
    directory = "C:Users/UserName/website.pdf"

    pdfName = "website.pdf"
    cheggLogin = 'https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F'

    pdf.from_url(url, 'website.pdf', configuration=config)
    #await ctx.send(file=discord.File('directory'))
