import asyncio


from array import array
from util import get_logger
from PLC.Rockwell.Watcher import rockwellWatcher

log = get_logger(__name__)

class Rockwell:
    def __init__(self, PLCIPs: array, rockwellTags: array):
        self._PLCIPs = PLCIPs
        self._rockwellTags = rockwellTags
        self._rockwellWatcher = rockwellWatcher(self._PLCIPs, self._rockwellTags)


    async def start(self):

        for self._plcip in self._PLCIPs:
            self._rockwellWatcher = rockwellWatcher(self._plcip, "Label_Print")

            asyncio.create_task(self._rockwellWatcher.start())
            
 


