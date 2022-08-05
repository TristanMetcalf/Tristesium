from array import array
import asyncio
from pycomm3 import LogixDriver
from eventStream.Producer import producer

from util import get_logger

log = get_logger(__name__)
 
class rockwellWatcher:

    def __init__(self, PLCIP:str, rockwellTag:str):

        self._PLCIP = PLCIP
        self._rockwellTag = rockwellTag

    async def start(self):
        asyncio.create_task(rockwellWatcher.watcher(self))
        print(f"Watching {self._PLCIP}") #log prints twice ???????

    async def watcher(self):
        try:
            with LogixDriver(self._PLCIP) as plc:
                tagValue = plc.read(self._rockwellTag)[1]
                log.info(f'Connected to {self._PLCIP} current tag is {tagValue}')
                while 1:
                    if tagValue != plc.read(self._rockwellTag)[1]:
                        tagValue = plc.read(self._rockwellTag)[1]
                        producer.addEvent(self,self._PLCIP, tagValue)

                    await asyncio.sleep(1)

                    if tagValue is None:
                        print(f"{self._PLCIP} tag doesnt exist")
                        return 0
        except Exception as Argument:
            print(Argument)
   
        