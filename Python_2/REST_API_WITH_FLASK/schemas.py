from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=Length(min=1, max=100))
    price = fields.Float(required=True, validate=Range(min=0))
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
