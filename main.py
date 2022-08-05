import configparser
from distutils.command.config import config
from PLC.Rockwell import Rockwell

from plex_api import PlexAPI
from PLC.Rockwell import Rockwell
from util import get_logger
import asyncio

log = get_logger(__name__)


class Tristesium:

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read("config.ini")
        self._tracked_plcs = self._config.get("PLC", "Tracked_plcs").split()
        self._tracked_tags = self._config.get("PLC", "PLCtags").split()

        self._plex_api = PlexAPI(self._config.get("Plex","test"), self._config.get("Plex","user"), self._config.get("Plex","passwd"))
        self._rockwell = Rockwell(self._tracked_plcs, self._tracked_tags)

    async def start(self):
        log.info("starting Tristesium")
        asyncio.ensure_future(self._plex_api.start())
        print(asyncio.ensure_future(self._rockwell.start()))



if __name__ == '__main__':
    flt = Tristesium()
    asyncio.ensure_future(flt.start())

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        log.info(f"Tristesium shutting down")