from marshmallow import fields, Schema
from schemas.director_schema import DirectorSchema

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    director_id = fields.Int(required=True, load_only=True)
    director = fields.Nested(DirectorSchema, dump_only=True)


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)