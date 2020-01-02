import discord
import asyncio


async def ex(args, message, client, invoke):

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2

    except:
        return

    failed = 0
    async for m in client.logs_from(message.channel, limit=ammount):
        try:
            await client.delete_message(m)
        except:
            pass
