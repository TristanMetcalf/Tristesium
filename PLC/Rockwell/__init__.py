import asyncio



from array import array
from util import get_logger
from PLC.Rockwell.Watcher import rockwellWatcher

log = get_logger(__name__)

class Rockwell:
    def __init__(self, PLCIPs: array, rockwellTags: array):


        self._PLCIPs = PLCIPs
        self._rockwellTags = rockwellTags


    async def start(self):
        log.info(self._PLCIPs)
        for plcip in self._PLCIPs:
            rockwellWatchers = rockwellWatcher(plcip, self._rockwellTags)
            asyncio.ensure_future(rockwellWatchers.start())
 


