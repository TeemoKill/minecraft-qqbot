from utils.request_utils import uuid2name
from config_manager import config

from nonebot import CommandSession

permissions = ('say', )
commands = ('say', 's')


async def get_command(session: CommandSession, parsed_message, command_say_bindings=None):
    if not command_say_bindings:
        command_say_bindings = config.command_say_bindings

    if session.event.user_id in command_say_bindings:
        sender_uuid = command_say_bindings[session.event.user_id]
        player_name = await uuid2name(sender_uuid)
        escaped_message = parsed_message.args.replace('\\', '\\\\').replace('"', '\\"')

        return f'tellraw @a {{"text": "*<{player_name}> {escaped_message}", "color": "yellow"}}', 'say'
    else:
        return '', 'You have no in-game character bound'


def parse_response(permission, response):
    if response == 'No player was found':
        return 'No player is online'
    else:
        return response
