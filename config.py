import json

class Config():
        with open("CommonSetting.json") as jsons:
            data = json.load(jsons)
        _Url = data["Url"]+":"+data["Port"]
        _Login = _Url+"/api/users/login"
        _getInventories = _Url+"/api/inventories"
        _editInventoryEmp = _Url+"/api/inventories/"
        _editInventoryCell = _Url+"/api/inventories/"
        _createStocks = _Url+"/api/stocks"
        _protocols = data["Protocol"]
        _getCellLine = _Url+"/api/cell-lines"
        _getReagentLine = _Url+"/api/culture-reagents"
        _cellLine = data["UsedCell"]
        _mediaLine = data["UsedMedia"]
        _trypsinLine = data["UsedTrypsin"]
        _cellBarcode = data["CellBarcode"]
        _trypsinBarcode = data["TrypsinBarcode"]
        _mediaBarcode = data["MediaBarcode"]
        _empPlateBarcode = data["EmptyPlateBarcode"]
        _empTroughBarcode = data["EmptyTroughBarcode"]
