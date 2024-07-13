import time

class GameDict:
    _instance = None
    started = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self.started:
            self.user = 'Dienekes'
            self.screen = 'Home'
            self.game_state = {}
            self.game_objects = []

            self.started

    def update(self, transaction):
        if screen_val := transaction.get('toSceneName'):
            self.screen = screen_val
        if match_val := transaction.get('matchGameRoomStateChangedEvent'):
            self.game_state = match_val
            self.screen = 'Playing' if self.playing else 'GameEnded'
        if gre_2_client := transaction.get('greToClientEvent',{}).get('greToClientMessages'):
            list(map(self.process_messages, gre_2_client))

        pass

    def process_messages(self,message):
        if game_objects := message.get('gameStateMessage',{}).get('gameObjects'):
            self.game_objects = game_objects
            print(game_objects)
            print()
        pass

    @property
    def playing(self):
        game_info = self.game_state.get('gameRoomInfo',{}).get('stateType')
        return True if game_info == 'MatchGameRoomStateType_Playing' else False
    @property
    def hero_seat(self):
        if players := self.game_state.get('gameRoomInfo',{}).get('players'):
            if players[0].get('playerName') == self.user:
                return players[0].get('teamId')
            if players[1].get('playerName') == self.user:
                return players[1].get('teamId')
    @property
    def villain_seat(self):
        if players := self.game_state.get('gameRoomInfo',{}).get('players'):
            if players[0].get('playerName') == self.user:
                return players[1].get('teamId')
            if players[1].get('playerName') == self.user:
                return players[0].get('teamId')


