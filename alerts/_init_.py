from .alerts import alerts

def setup(bot):
    cog = alerts(bot)
    bot.add_cog(cog)
