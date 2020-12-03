from .autoreact import autoreact

def setup(bot):
    cog = autoreact(bot)
    bot.add_cog(cog)
