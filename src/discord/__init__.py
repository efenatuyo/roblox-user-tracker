import discord
from discord.ext import commands

from ..database import r, w, a
from ..requestHandler import user_request
from ..misc import u

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command(name="add_monitor")
async def add_monitor(ctx, user_id="", channel_id=""):
    if not ctx.author.guild_permissions.administrator:
        return await ctx.reply("Administrator required to use this command")
    
    if not user_id.isdigit():
        if not user_id:
            return await ctx.reply("A user id must be provided")
        return await ctx.reply("User id has to be a number")
    
    if not channel_id.isdigit():
        if not channel_id:
            return await ctx.reply("A channel id must be provided")
        return await ctx.reply("Channel id has to be a number")
    
    channel = bot.get_channel(int(channel_id))
    if not (channel and channel.guild.id == ctx.guild.id):
        return await ctx.reply("Channel id has to be located in this guild")
    
    if not channel.permissions_for(ctx.me).send_messages:
        return await ctx.reply("Send messages permission required for the bot")
    
    if not channel.permissions_for(ctx.me).embed_links:
        return await ctx.reply("Embed links permission required for the bot")
    
    data = r()
    if str(user_id) in data["users_track"]:
        if int(channel_id) in data["users_track"][str(user_id)]["channel_message"]:
            return await ctx.reply("This channel already monitors this id")
        data["users_track"][str(user_id)]["channel_message"].append(int(channel_id))
        data["users_track"][str(user_id)] = {"online_status": data["users_track"][str(user_id)]["online_status"], "channel_message": data["users_track"][str(user_id)]["channel_message"]}
        w(data)
    else:
        u(user_request(user_id=int(user_id), online_status=0), data, id=int(channel_id))
    
    return await ctx.reply(f"Started monitoring user id: **{user_id}** in channel id: **{channel_id}**")

@bot.command(name="remove_monitor")
async def remove_monitor(ctx, user_id, channel_id):
    if not ctx.author.guild_permissions.administrator:
        return await ctx.reply("Administrator required to use this command")
    
    if not user_id.isdigit():
        if not user_id:
            return await ctx.reply("A user id must be provided")
        return await ctx.reply("User id has to be a number")
    
    if not channel_id.isdigit():
        if not channel_id:
            return await ctx.reply("A channel id must be provided")
        return await ctx.reply("Channel id has to be a number")
    
    channel = bot.get_channel(int(channel_id))
    if not (channel and channel.guild.id == ctx.guild.id):
        return await ctx.reply("Channel id has to be located in this guild")
    
    data = r()
    if str(user_id) in data["users_track"]:
        if int(channel_id) in data["users_track"][str(user_id)]["channel_message"]:
            data["users_track"][str(user_id)]["channel_message"].remove(int(channel_id))
            a({"users_track": {str(user_id): {"online_status": data["users_track"][str(user_id)]["online_status"], "channel_message": data["users_track"][str(user_id)]["channel_message"]}}})
        else:
            return await ctx.reply("User id doesn't get monitored in the channel")
    else:
        return await ctx.reply("User id doesn't get monitored")
    
    return await ctx.reply(f"Removed monitoring for user id: **{str(user_id)}** in channel id: **{str(channel_id)}**")