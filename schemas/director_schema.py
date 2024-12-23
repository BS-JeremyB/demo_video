from marshmallow import Schema, fields

class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)