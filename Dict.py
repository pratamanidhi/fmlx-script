import re


class Dict():
    def _Login():
        payload = {
            "userName": "admin",
            "password": "admin"
        }
        return payload
    
    def _inventoryId(_id):
        payload = {
            "id" : _id
        }
    
    def _inventorySize():
        payload = {
            "PageSize" : "1000"
        }
        return payload

    def _setEmpty():
        payload = {
            "labwareId": 1,
            "contentType": "Empty",
            "isPreBarcoded": "false",
            "notes": "EmptyCell",
            "contents": [],
            "quantity": 1,
            "isPrintBarcode": "false"
        }
        return payload
    
    def _setCell(_id):
        payload = {
            "labwareId": 1,
            "contentType": "Cell",
            "isPreBarcoded": "false",
            "notes": "CellLine1",
            "contents": [
                {
                "volume": 15000,
                "wellName": "A1",
                "color": "#F4C7AB",
                "cellLineId": int(_id)
                }
            ],
            "quantity": 1,
            "isPrintBarcode": "false"
        }
        return payload

    def _setMedia(_id):
        payload = {
            "labwareId": 4,
            "contentType": "Reagent",
            "expirationDate": "2026-08-08T03:14:57.255Z",
            "isPreBarcoded": "false",
            "notes": "Trough Media",
            "contents": [
                {
                "volume": 250000,
                "wellName": "A1",
                "color": "#D5EEBB",
                "cultureReagentId": int(_id)
                }
            ],
            "quantity": 1,
            "storeTemperature": "Refrigerator",
            "isPrintBarcode": "false"
        }
        return payload

    def _setTrypsin(_id):
        payload = {
            "labwareId": 4,
            "contentType": "Reagent",
            "expirationDate": "2026-08-08T03:14:57.255Z",
            "isPreBarcoded": "false",
            "notes": "Trough Media",
            "contents": [
                {
                "volume": 250000,
                "wellName": "A1",
                "color": "#D5EEBB",
                "cultureReagentId": int(_id)
                }
            ],
            "quantity": 1,
            "storeTemperature": "Refrigerator",
            "isPrintBarcode": "false"
        }
        return payload

    def _setEmpTrough():
        payload = {
            "labwareId": 4,
            "contentType": "Empty",
            "isPreBarcoded": "false",
            "notes": "",
            "contents": [],
            "quantity": 1,
            "isPrintBarcode": "false"
        }
        return payload

    def _setTipCaddy():
        payload = {
            "labwareId": 6,
            "contentType": "Tip",
            "isPreBarcoded": "false",
            "notes": "Tip Caddy",
            "contents": [],
            "quantity": 1,
            "tipAmount": 96,
            "isPrintBarcode": "false"
        }
        return payload

    def _feeding(_id):
        payload = {
            "name": "TestFeeding",
            "quantity": 1,
            "sourceId": int(_id),
            "feedingProfileId": 3,
            "formulateMediaProfileId": 7,
            "enzymeDigestionProfileId": 1,
            "imagingConfluencyProfileId": 2,
            "passageProfileId": 5,
            "motionProfileId": 2,
            "cultureMethod": {
                "isWashWithPbs": "false",
                "totalVolume": 10000,
                "passageAfterConfluencyPercentage": 80,
                "passageAfterTimeIntervalHour": None,
                "mediaCultureReagentId": 8,
                "mediaReplacementPercentage": 100,
                "feedingIntervalHour": 1,
                "enzymeCultureReagentId": 2,
                "enzymeVolumeMicroLiter": 5000,
                "enzymeIncubationTimeMinute": 5,
                "passageRatio": 6,
                "incubationTimeAfterPassageHour": 6,
                "imagingIntervalHour": 1
            }
        }
        return payload

    def _passaging(_id):
        payload = {
        "name": "TestPAssaging",
        "quantity": 1,
        "sourceId": int(_id),
        "feedingProfileId": 6,
        "formulateMediaProfileId": 4,
        "enzymeDigestionProfileId": 7,
        "imagingConfluencyProfileId": 2,
        "passageProfileId": 5,
        "motionProfileId": 3,
        "cultureMethod": {
                "isWashWithPbs": "false",
                "totalVolume": 1500,
                "passageAfterConfluencyPercentage": None,
                "passageAfterTimeIntervalHour": 2,
                "mediaCultureReagentId": 8,
                "mediaReplacementPercentage": 100,
                "feedingIntervalHour": 12,
                "enzymeCultureReagentId": 3,
                "enzymeVolumeMicroLiter": 5000,
                "enzymeIncubationTimeMinute": 5,
                "passageRatio": 6,
                "incubationTimeAfterPassageHour": 6,
                "imagingIntervalHour": None
            }
        }
        return payload
