
from . import vc_asst, get_string, list_queue, VC_QUEUE


@vc_asst("queue")
async def lstqueue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    q = list_queue(chat)
    if not q:
        return await event.eor(get_string("vcbot_21"))
    await event.eor(f"• <strong>Queue:</strong>\n\n{q}", parse_mode="html")


@vc_asst("clearqueue")
async def clean_queue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    if VC_QUEUE.get(chat):
        VC_QUEUE.pop(chat)
    await event.eor(get_string("vcbot_22"), time=5)
