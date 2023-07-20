import discord
from discord.ext import commands

from config import DISCORD_TOKEN
from riotwatcher import RiotWatcher

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

async def get_match_list(summoner_name: str, region: str, watcher: RiotWatcher):
    # Ottieni la lista delle partite recenti del giocatore
    matches = await watcher.get_match_list(summoner_name)

    # Mostra il nome, la data, l'ora e la durata di ogni partita
    for match in matches:
        await ctx.send(f"Nome: {match.name}\nData: {match.date}\nOra: {match.time}\nDurata: {match.duration}")

@bot.command(name="profile")
async def profile(ctx, summoner_name):
    # Ottieni il profilo del giocatore
    profile = await watcher.get_summoner(summoner_name)

    # Mostra il nome, il livello e il punteggio di maestria del giocatore
    await ctx.send(f"Nome: {profile.name}\nLivello: {profile.level}\nMaestria: {profile.mastery_points}")

@bot.command(name="rank")
async def rank(ctx, summoner_name):
    # Ottieni la classifica del giocatore
    rank = await watcher.get_league_by_summoner(summoner_name)

    # Mostra il nome, la divisione e il punteggio di classifica del giocatore
    await ctx.send(f"Nome: {rank.summoner.name}\nDivisione: {rank.tier} {rank.division}\nPunteggio: {rank.league_points}")

@bot.command(name="matches")
async def matches(ctx, summoner_name):
    # Ottieni la lista delle partite recenti del giocatore
    matches = await watcher.get_match_list(summoner_name)

    # Mostra il nome, la data, l'ora e la durata di ogni partita
    for match in matches:
        await ctx.send(f"Nome: {match.name}\nData: {match.date}\nOra: {match.time}\nDurata: {match.duration}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
