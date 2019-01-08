from pyiex_config import *


def sectorPerformance(sector=None):
    sectorDict = {}
    iDict = {}
    resp_str = requests.get(base_url + version +
               "/stock/market/sector-performance").json()
    if sector == None:
        for i in resp_str:
            iDict[i["name"]] = i["performance"]
        return iDict
    else:
        for i in resp_str:
            if i["name"] == sector:
                iDict[i["name"]] = i["performance"]
                return iDict
            else:
                pass


def listsymbols(sector=None):
        sectorDict = sectorPerformance(sector)
        if sector == None:
            symbolList = []
            for value in sectorDict:
                resp_str = requests.get(base_url + version +
                           "/stock/market/collection/sector?collectionName=" +
                           value["name"]).json()
                for y in resp_str:
                    symbolList.append(y["ticker"])
            return symbolList
        else:
            symbolList = []
            resp_str = requests.get(base_url + version +
                       "/stock/market/collection/sector?collectionName=" +
                       sector).json()
            for y in resp_str:
                symbolList.append(y["ticker"])
            return symbolList 
