import pdfkit as pdf

#where bot saves the file
directory = "C:Users/UserName/website.pdf"

pdfName = "website.pdf"
cheggLogin = 'https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F'

def fileUpload(ctx, url):
    pdf.from_url(url, 'website.pdf', configuration=config)
    await ctx.send(file=discord.File('directory'))
