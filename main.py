import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# BASIC SETUP
# =========================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx, type=None):

    if type is None:
        await ctx.send("Usage: !setup basic / normal / legendary")
        return

    guild = ctx.guild

    # =========================
    # BASIC SERVER
    # =========================
    if type.lower() == "basic":

        category = await guild.create_category("📘 BASIC SERVER")

        await guild.create_text_channel("rules", category=category)
        await guild.create_text_channel("general", category=category)
        await guild.create_text_channel("media", category=category)

        role = await guild.create_role(name="Member")

        await ctx.send("✅ Basic server setup completed 😄")

    # =========================
    # NORMAL SERVER
    # =========================
    elif type.lower() == "normal":

        info = await guild.create_category("📌 INFORMATION")
        chat = await guild.create_category("💬 CHATS")
        vc = await guild.create_category("🎤 VOICE CHANNELS")

        await guild.create_text_channel("rules", category=info)
        await guild.create_text_channel("announcements", category=info)
        await guild.create_text_channel("server-updates", category=info)

        await guild.create_text_channel("general", category=chat)
        await guild.create_text_channel("memes", category=chat)
        await guild.create_text_channel("media", category=chat)
        await guild.create_text_channel("bot-commands", category=chat)

        await guild.create_voice_channel("General VC", category=vc)
        await guild.create_voice_channel("Gaming VC", category=vc)

        await guild.create_role(name="Owner", color=discord.Color.red())
        await guild.create_role(name="Moderator", color=discord.Color.blue())
        await guild.create_role(name="Member", color=discord.Color.green())

        await ctx.send("🔥 Normal server setup completed 😈")

    # =========================
    # LEGENDARY SERVER
    # =========================
    elif type.lower() == "legendary":

        owner = await guild.create_role(
            name="👑 Owner",
            color=discord.Color.gold()
        )

        admin = await guild.create_role(
            name="⚡ Admin",
            color=discord.Color.red()
        )

        mod = await guild.create_role(
            name="🛡️ Moderator",
            color=discord.Color.blue()
        )

        vip = await guild.create_role(
            name="💎 VIP",
            color=discord.Color.purple()
        )

        member = await guild.create_role(
            name="🌟 Member",
            color=discord.Color.green()
        )

        info = await guild.create_category("📢 SERVER INFO")
        community = await guild.create_category("💬 COMMUNITY")
        media = await guild.create_category("🎬 MEDIA")
        gaming = await guild.create_category("🎮 GAMING")
        voice = await guild.create_category("🎤 VOICE CHANNELS")
        staff = await guild.create_category("🛠️ STAFF")

        await guild.create_text_channel("rules", category=info)
        await guild.create_text_channel("announcements", category=info)
        await guild.create_text_channel("giveaways", category=info)
        await guild.create_text_channel("server-news", category=info)

        await guild.create_text_channel("general", category=community)
        await guild.create_text_channel("introductions", category=community)
        await guild.create_text_channel("memes", category=community)
        await guild.create_text_channel("chat", category=community)

        await guild.create_text_channel("photos", category=media)
        await guild.create_text_channel("videos", category=media)
        await guild.create_text_channel("artwork", category=media)

        await guild.create_text_channel("gaming-chat", category=gaming)
        await guild.create_text_channel("clips", category=gaming)
        await guild.create_text_channel("looking-for-group", category=gaming)

        await guild.create_voice_channel("General VC", category=voice)
        await guild.create_voice_channel("Gaming VC", category=voice)
        await guild.create_voice_channel("Music VC", category=voice)
        await guild.create_voice_channel("Chill VC", category=voice)

        await guild.create_text_channel("staff-chat", category=staff)
        await guild.create_text_channel("mod-logs", category=staff)

        await ctx.send("👑 LEGENDARY SERVER CREATED 😈🔥")

    else:
        await ctx.send("❌ Choose: basic / normal / legendary")

# =========================
# ERROR HANDLER
# =========================
@setup.error
async def setup_error(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You need administrator permission!")

# =========================
# RUN BOT
# =========================
bot.run(os.getenv("DISCORD_TOKEN"))
