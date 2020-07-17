from utils.mc_utils import get_server


def test_get_server():
    server_properties = {
        'vanilla': {'address': 'host', 'rcon_port': 25575, 'rcon_password': 'super secret', 'aka': ['v']}}
    assert get_server('add', 'vanilla', server_properties) == ('add', ['vanilla'])
    assert get_server('add @vanilla', 'vanilla', server_properties) == ('add', ['vanilla'])
    assert get_server('add @v', 'vanilla', server_properties) == ('add', ['vanilla'])
