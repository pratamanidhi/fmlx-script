import json
from config import Config as _config
from Suite import Suite as _suite
import time
from Utils import  Utils as _utils

if __name__ == "__main__":
    _utils.Initiate_Script
    print("------- Sistem Login Started -------")
    login = _suite._Login()
    print("")
    print("------- Start Edit Cell Lines -------")
    _suite._getInventoryCellLine(login)
    print("")
    print("------- Start Edit Empty Plate -------")
    _suite._getInventoriesEmpPlate(login)
    print("")
    print("------- Start Edit Media -------")
    _suite._getInventoryMedia(login)
    print("")
    print("------- Start Edit Trypsin -------")
    _suite._getInventoryTrypsin(login)
    print("")
    print("------- Start Edit Empty Trough -------")
    _suite._getInventoryEmpT(login)
    print("")
    print("------- Start Edit Tip Caddy -------")
    _suite._getInventoryCaddy(login)

    #print("=== wait for 10 minutes ===")
    #time.sleep(600)
    # print("")
    # print("== Start Register Protocols ==")
    # _suite._getCellLines(login)
    # _suite._getCellLine(login)
    _utils.Finist_Script
