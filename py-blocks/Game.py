import Utils as Utils
import requests
import User as Internal
import Game as External
from typing import Union, Type

#Personal Game Vars
class MyGame(object):
    def __init__(self):
        self.maxPlayerCount = None
        self.socialSlotType = None
        self.customSocialSlotsCount = None
        self.allowCopying = None
        self.currentSavedVersion = None
        self.name = None
        self.isRootPlace = None
        self.descriptionisRootPlace = None

def GetUniverseID(PlaceID: int) -> Union[int, str]:
    """
    Returns the universe id for the given game (if any)
    """
    try:
        response = Internal.CurrentCookie.get(f"{Utils.GamesAPI}games/multiget-place-details?placeIds={str(PlaceID)}")
        try:
            return response.json()['data'][0]
        except:
            return 'Universe Not Found'
    except Exception as e:
        return e

def GetCurrentPlayers(PlaceID: int) -> Union[int, str]:
    """
    Returns the number of players in the given game
    """
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetCurrentUniversePlayers(UniverseID)
        return GameData['playing']
    except:
        return "Error"

def GetGameVisits(PlaceID: int) -> Union[int, str]:
    """
    Returns the number of players that have visited the given game
    """
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetUniverseData(UniverseID)
        return GameData['visits']
    except:
        return "Error"

def GetGameLikes(PlaceID: int) -> Union[int, str]:
    """
    Returns the number of likes for the given game
    """
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['upVotes']
    except:
        return "Error"

def GetGameDislikes(PlaceID: int) -> Union[int, str]:
    """
    Returns the number of dislikes for the given game
    """
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['downVotes']
    except:
        return "Error"

def GetGameFavourites(PlaceID: int) -> Union[int, str]:
    """
    Returns the number of players that have favoutited the given game
    """
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseFavourites(UniverseID)
    except:
        return "Error"

def GetMyGameData(PlaceID: int) -> Union[Type[MyGame], str]:
    """
    Returns data for your specified game
    """
    try:
        response = Internal.CurrentCookie.get(Utils.DevelopAPIV2 + f"places/{PlaceID}")
        game = MyGame()
        game.maxPlayerCount = response.json()['maxPlayerCount']
        game.socialSlotType = response.json()['socialSlotType']
        game.customSocialSlotsCount = response.json()['customSocialSlotsCount']
        game.allowCopying = response.json()['allowCopying']
        game.currentSavedVersion = response.json()['currentSavedVersion']
        game.name = response.json()['name']
        game.descriptionisRootPlace = response.json()['description']
        game.isRootPlace = response.json()['isRootPlace']
        return game
    except:
        return response.json()['errors'][0]['message']

def GetUniverseData(UniverseID: int) -> Union[dict, str]:
    """
    Returns the returns the raw json for the given universe
    """
    response = requests.get(f"{Utils.GamesAPI}games?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseVotes(UniverseID: int) -> Union[dict, str]:
    """
    Returns the number of likes and dislikes for the given universe
    """
    response = requests.get(f"{Utils.GamesAPI}games/votes?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseFavourites(UniverseID: int) -> Union[int, str]:
    """
    Returns the number of players that have favoutited the given universe
    """
    response = requests.get(f"{Utils.GamesAPI}games/{str(UniverseID)}/favorites/count")
    try:
        return response.json()['favoritesCount']
    except:
        return 'Universe Not Found'

def GetCurrentUniversePlayers(UniverseID: int) -> Union[int, str]:
    """
    Returns the number of players in the given universe
    """
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['playing']
    except:
        return 'Universe Not Found'

def GetUniverseVisits(UniverseID: int) -> Union[int, str]:
    """
    Returns the number of players that have visited the given universe
    """
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['visits']
    except:
        return 'Universe Not Found'

def GetUniverseLikes(UniverseID: int) -> Union[int, str]:
    """
    Returns the number of likes for the given universe
    """
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['upVotes']
    except:
        return 'Universe Not Found'

def GetUniverseDislikes(UniverseID: int) -> Union[int, str]:
    """
    Returns the number of dislikes for the given universe
    """
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['downVotes']
    except:
        return 'Universe Not Found'