from utilities import BiDict

packets = BiDict({
    'protocol_request': 0,
    'protocol_response': 1,
    'server_disconnect': 2,
    'connect_success': 3,
    'connect_failure': 4,
    'handshake_challenge': 5,
    'chat_received': 6,
    'universe_time_update': 7,
    'celestial_response': 8,
    'player_warp_result': 9,
    'client_connect': 10,
    'client_disconnect_request': 11,
    'handshake_response': 12,
    'player_warp': 13,
    'fly_ship': 14,
    'chat_sent': 15,
    'celestial_request': 16,
    'client_context_update': 17,
    'world_start': 18,
    'world_stop': 19,
    'central_structure_update': 20,
    'tile_array_update': 21,
    'tile_update': 22,
    'tile_liquid_update': 23,
    'tile_damage_update': 24,
    'tile_modification_failure': 25,
    'give_item': 26,
    'environment_update': 27,
    'entity_interact_result': 28,
    'update_tile_protection': 29,
    'set_player_start': 30,
    'find_unique_entity_response': 31,
    'modify_tile_list': 32,
    'damage_tile_group': 33,
    'collect_liquid': 34,
    'request_drop': 35,
    'spawn_entity': 36,
    'entity_interact': 37,
    'connect_wire': 38,
    'disconnect_all_wires': 39,
    'world_client_state_update': 40,
    'find_unique_entity': 41,
    'entity_create': 42,
    'entity_update': 43,
    'entity_destroy': 44,
    'hit_request': 45,
    'damage_request': 46,
    'damage_notification': 47,
    'entity_message': 48,
    'entity_message_response': 49,
    'update_world_properties': 50,
    'step_update': 51})

entity_type = BiDict({
    'end': -1,
    'player': 0,
    'monster': 1,
    'object': 2,
    'itemdrop': 3,
    'projectile': 4,
    'plant': 5,
    'plantdrop': 6,
    'effect': 7,
    'npc': 8})

