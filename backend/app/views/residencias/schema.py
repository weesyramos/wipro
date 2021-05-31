from marshmallow import Schema, fields


class RequestResidenciasSchema(Schema):
    pass



class ResponseResidenciasSchema(Schema):
    id = fields.Integer()
    username = fields.String()