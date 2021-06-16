import pdfkit as pdf

def fileUpload(ctx, url):
    pdf.from_url(url, 'website.pdf', configuration=config)
    await ctx.send(file=discord.File('C:/Users/UserName/website.pdf'))