import json
import xml.etree.ElementTree as et


class Appartment:
    def __init__(self, house_id, used, bill):
        self.house_id = house_id
        self.used = used
        self.bill = bill

    def show(self,data):
        return type(data.house_id), type(data.used), type(data.bill)


class BillSerializer:
    def serialize(self, used, format):
        serializer = self._get_serializer(format)
        return serializer(used)

    def _get_serializer(self, format):
        if format == 'house':
            return self._serialize_to_house
        elif format == 'company':
            return self._serialize_to_company
        else:
            raise ValueError(format)

    def _serialize_to_house(self, used):
        payload = {
            'id': used.house_id,
            'used': used.used,
            'bill': used.bill * used.used
        }
        return json.dumps(payload)

    def _serialize_to_company(self, use):
        payload = {
            'id': use.house_id,
            'used': use.used,
            'bill': use.bill * use.used *1.4
        }
        return payload


app = Appartment(1, 123.7, 13)
print(app.show(app))
serializer = BillSerializer()
print(serializer.serialize(app, 'house'))
print(serializer.serialize(app, 'company'))
