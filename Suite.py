from email import header
import json
from re import search
import requests
from config import Config as _config
from Dict import Dict as _dict
import time

class Suite():
    def __init__(self) -> None:
        pass

    def _Login():
        _request = requests.post(
            _config._Login,
            json=_dict._Login()
        )
        _response = _request.json().get("token")
        print("== Login Success ==")
        return _response


    def _getInventoriesEmpPlate(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            barcode = i["barcode"]
            if search(_config._empPlateBarcode,barcode):
                _id = i["id"]
                a = Suite()
                a._inventoryEditEmp(_token,str(_id))
        return parse

    def _getInventoryCellLine(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            barcode = i["barcode"]
            if search(_config._cellBarcode,barcode):
                _id = i["id"]
                print(barcode)
                a = Suite()
                a._inventoryCell(_token,str(_id))
        return parse

    def _getInventoryMedia(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            barcode = i["barcode"]
            if search(_config._mediaBarcode,barcode):
                _id = i["id"]
                a = Suite()
                a._invetoryMedia(_token,str(_id))
        return parse

    def _getInventoryTrypsin(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            barcode = i["barcode"]
            if search(_config._trypsinBarcode,barcode):
                _id = i["id"]
                a = Suite()
                a._invetoryTrypsin(_token,str(_id))
        return parse

    def _getInventoryEmpT(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            barcode = i["barcode"]
            if search(_config._empTroughBarcode,barcode):
                _id = i["id"]
                a = Suite()
                a._invetoryEmpT(_token,str(_id))
        return parse

    def _getInventoryCaddy(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            barcode = i["barcode"]
            a = Suite()
            if search("TIPC",barcode) and search("TIP", barcode):
                _id = i["id"]
                a._invetoryCaddy(_token,str(_id))
            if search("TIP", barcode):
                _id = i["id"]
                a._invetoryCaddy(_token, str(_id))
        return parse

    def _inventoryEditEmp(self, _token,_id):
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request = requests.put(
            _config._editInventoryEmp+_id,
            headers=_header,
            json=_dict._setEmpty()
        )
        if request.status_code == 204:
            print("== Empty Plate Registered ==")
            return request.status_code
        print("== Empty Plate Fail ==")

    def _inventoryCell(self, _token,_id):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request_cell = requests.get(
            _config._getCellLine,
            headers = _header
        )
        for i in request_cell.json():
            if i["name"] == _config._cellLine:
                print("=== Cell Found !! ===")
                id = i["id"]
                parse.append(id)
        request = requests.put(
            _config._editInventoryCell+_id,
            headers=_header,
            json=_dict._setCell(parse[0])
        )
        if request.status_code == 204:
            print("== Cell Plate Registered ==")
            return request.status_code
        print("== Cell Plate Fail ==")

    def _invetoryMedia(self, _token, _id):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request_media = requests.get(
            _config._getReagentLine,
            headers = _header
        )
        for i in request_media.json():
            if i["name"] == _config._mediaLine:
                print("=== Media Found !! ===")
                id = i["id"]
                parse.append(id)
        request = requests.put(
            _config._editInventoryCell+_id,
            headers=_header,
            json=_dict._setMedia(parse[0])
        )
        if request.status_code == 204:
            print("== Media Registered ==")
            return request.status_code
        print("== Media Fail ==")

    def _invetoryTrypsin(self, _token, _id):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request_Trypsin = requests.get(
            _config._getReagentLine,
            headers = _header
        )
        for i in request_Trypsin.json():
            if i["name"] == _config._trypsinLine:
                print("=== Trypsin Found !! ===")
                id = i["id"]
                parse.append(id)
        request = requests.put(
            _config._editInventoryCell+_id,
            headers=_header,
            json=_dict._setTrypsin(parse[0])
        )
        if request.status_code == 204:
            print("== Trypsin Registered ==")
            return request.status_code
        print("== Trypsin Fail ==")

    def _invetoryEmpT(self, _token, _id):
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request = requests.put(
            _config._editInventoryCell+_id,
            headers=_header,
            json=_dict._setEmpTrough()
        )
        if request.status_code == 204:
            print("== Empty Trough Registered ==")
            return request.status_code
        print("== Empty Trough Fail ==")

    def _invetoryCaddy(self, _token, _id):
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request = requests.put(
            _config._editInventoryCell+_id,
            headers=_header,
            json=_dict._setTipCaddy()
        )
        if request.status_code == 204:
            print("== Tip Caddy Registered ==")
            return request.status_code
        print("== Tip Caddy Fail ==")

    def _getCellStatus(_token):
        parse = []
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        for i in request.json():
            if search(_config._cellBarcode, i["barcode"]):
                _status = i["status"]
                _locations = i["currentLocation"]
                if (_status == "Available") and search("Incubator", _locations):
                    parse.append(True)
                else:
                    parse.append(False)
        return parse

    def _getCellLines(_token):
        _header = {
            "Authorization" : "Bearer "+_token
            }
        request = requests.get(
            _config._getInventories,
            headers=_header,
            params=_dict._inventorySize()
        )
        parse = []
        a = Suite()
        for i in request.json():
            if i["contentType"] == "Cell":
                print(f" Cell Line Barcode Found!!, Barcode : {i['barcode']}")
                _id = i["id"]
                parse.append(_id)
        a.FeedingPassaging(parse,_token)

    def FeedingPassaging(self,_task,_token):
        a = Suite()
        if _config._protocols == "Feeding":
            for i in _task:
                a._startFeeding(_token, i)
        elif _config._protocols == "Passaging":
            for i in _task:
                a._startPassaging(_token, i)
        else:
            print("==== Initiate Feeding and Passagig Protocols ====")
            for i in _task:
                if(i % 2) == 0:
                    print("==== Feeding Protocols Start ====")
                    a._startFeeding(_token,i)
                else:
                    print("==== Passaging Protocols Start ====")
                    a._startPassaging(_token, i)


    def _startFeeding(self, _token, _id):
        print("== Generating Feeding Protocols ==")
        parse = []
        cultureReagent = []
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request_try = requests.get(
            _config._getReagentLine,
            headers = _header
        )
        for j in request_try.json():
            if j["name"] == _config._trypsinLine:
                print("=== Trypsin Found !! ===")
                id = j["id"]
                cultureReagent.append(id)
        request_media = requests.get(
            _config._getReagentLine,
            headers = _header
        )
        for i in request_media.json():
            if i["name"] == _config._mediaLine:
                print("=== Media Found !! ===")
                id = i["id"]
                parse.append(id)
        _request = requests.post(
            _config._createStocks,
            headers=_header,
            json=_dict._feeding(_id,parse[0],cultureReagent[0])
        )
        if _request.status_code == 201:
            print("== Stock Created ==")
            return _request.status_code
        print("== Stock Failed ==")

    def _startPassaging(self, _token, _id):
        print(f"== Generating Passaging Protocols ==")
        parse = []
        cultureReagent = []
        _header = {
            "Authorization" : "Bearer "+_token
        }
        request_try = requests.get(
            _config._getReagentLine,
            headers = _header
        )

        for j in request_try.json():
            if j["name"] == _config._trypsinLine:
                print("=== Trypsin Found !! ===")
                id = j["id"]
                cultureReagent.append(id)

        request_media = requests.get(
            _config._getReagentLine,
            headers = _header
        )

        for i in request_media.json():
            if i["name"] == _config._mediaLine:
                print("=== Media Found !! ===")
                id = i["id"]
                parse.append(id)

        _request = requests.post(
            _config._createStocks,
            headers=_header,
            json=_dict._passaging(_id,parse[0],cultureReagent[0])
        )

        if _request.status_code == 201:
            print("== Stock Created ==")
            return _request.status_code
        print("== Stock Failed ==")

    def _changeMultiplier(_token):
        _header = {
            "Authorization" : "Bearer "+_token
        }
        _request = requests.put(
            _config._setNewMultipler,
            headers = _header,
            json=_dict._setMultiplier(str(_config._systemMultiplier))
        )
        if _request.status_code == 204:
            print(f"=== System accelerate {str(_config._systemMultiplier)} times ===")
        else:
            print("== Failed to accelerate the system ==")

