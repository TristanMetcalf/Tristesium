import urllib.request as urllib2

from suds.transport.https import HttpAuthenticated
from suds.client import Client


from util import get_logger

log = get_logger(__name__)

class PlexAPI:
    def __init__(self, server:str, user:str, passwd:str):
        self._server = server
        self._user = user
        self._passwd = passwd


        self._t = HttpAuthenticated(username=self._user, password=self._passwd)
        self._t.handler = urllib2.HTTPBasicAuthHandler(self._t.pm)
        self._t.urlopener = urllib2.build_opener(self._t.handler)
        self._c = Client(url=self._server,transport=self._t)


    async def start(self):
        log.info("Starting Plex API")
        log.info("Started plex API")

    async def recordProduction(self, PLC):
        nameString = "@Result_Message,@PLC_Name,@Output_Stream_Id"
        valueString = "True," + PLC + ",1"
        print(valueString)
        webreq = self._c.service.ExecuteDataSourcePost(21443, nameString, valueString, ",") #Datasourceint Namesstring Valuesstring delimiter
        print(webreq)
        for web in webreq["OutputParameters"][0]:
            match web.Name:
                case "@Result_Message":
                    result = web.Value
                case "@Recorded_Quantity":
                    qty = web.Value
                case "@Result_Error":
                    error = web.Value
                case "@Recorded_Serial_No":
                    serial = web.Value
                case "@Recorded_Part_No":
                    part_no = web.Value
                case "@Recorded_Revision":
                    revision = web.Value
            return {"qtyrecorded":qty,"result":result,"error":error,"serialNumber":serial,"Part_No":part_no,"revision":revision}

    async def getLabel(self, serial):
        webreq = self._c.service.ExecuteDataSourcePost(1953,"SerialNo",serial,",")
        for web in webreq["OutputParameters"][0]:
            match web.Name:
                case "Label":
                    label = web.Value
                case "Printer":
                    printer = web.Value
                case "ResultError":
                    error = web.Value
                case "ResultMessage":
                    ResultMessage = web.Value
                case "ResultCode":
                    ResultCode = web.Value
        return {"label":label,"printer":printer,"error":error,"resultmessage":ResultMessage,"resultCode":ResultCode}

    def getWorkcenterbyKey(self, key):

        data = dict()
        res = self._c.service.ExecuteDataSourcePost(6057,"Workcenter_Key", key,",")
    

        for i in res['ResultSets'].ResultSet[0].Rows[0][0][0].Column:

            data.update({i.Name:i.Value})

        return data