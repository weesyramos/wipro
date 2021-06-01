from marshmallow import Schema, fields


class RequestResidenciasSchema(Schema):
    id = fields.String() 
    name = fields.String() 	
    host_id	 = fields.String() 
    host_name = fields.String() 	
    neighbourhood = fields.String() 	
    latitude = fields.String() 	
    longitude = fields.String() 	
    room_type = fields.String() 	
    price = fields.String() 	
    minimum_nights = fields.String() 	
    number_of_reviews = fields.String() 	
    last_review = fields.String() 	
    reviews_per_month = fields.String() 	
    calculated_host_listings_count = fields.String() 	
    availability_365 = fields.String() 	
    neighbourhood_group = fields.String() 



class ResponseResidenciasSchema(Schema):
    id = fields.String() 
    name = fields.String() 	
    host_id	 = fields.String() 
    host_name = fields.String() 	
    neighbourhood = fields.String() 	
    latitude = fields.String() 	
    longitude = fields.String() 	
    room_type = fields.String() 	
    price = fields.String() 	
    minimum_nights = fields.String() 	
    number_of_reviews = fields.String() 	
    last_review = fields.String() 	
    reviews_per_month = fields.String() 	
    calculated_host_listings_count = fields.String() 	
    availability_365 = fields.String() 	
    neighbourhood_group = fields.String() 
