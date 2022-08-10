from array import array
import asyncio
from pycomm3 import LogixDriver
from eventStream.Producer import producer

from util import get_logger

log = get_logger(__name__)
 
class rockwellWatcher:

    def __init__(self, PLCIP:str, rockwellTags:array):

        self._PLCIP = PLCIP
        self._rockwellTags = rockwellTags

    async def start(self):
        await self.watcher() 

    async def watcher(self):
        try:
            with LogixDriver(self._PLCIP) as plc:
                
                print(f'Connected to {self._PLCIP}')

                while 1:
                    print(plc.read(*self._rockwellTags))

                    await asyncio.sleep(.1)

        except Exception as Argument:
            print(Argument)
   
        