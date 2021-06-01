from flask import current_app

from backend.app.views.residencias.schema import ResponseResidenciasSchema
from backend.core.models.model_residencias import ModelResidencias



class ServiceResidencias:

    @staticmethod
    def list_residencias(**schema):
        import ipdb; ipdb.set_trace()
        name = schema.get('name', False) 	
        host_id	 = schema.get('host_id', False) 
        host_name = schema.get('host_name', False) 	
        neighbourhood = schema.get('neighbourhood', False) 	
        latitude = schema.get('latitude', False) 	
        longitude = schema.get('longitude', False) 	
        room_type = schema.get('room_type', False) 	
        price = schema.get('price', False) 	
        minimum_nights = schema.get('minimum_nights', False) 	
        number_of_reviews = schema.get('number_of_reviews', False) 	
        last_review = schema.get('nlast_reviewame', False) 	
        reviews_per_month = schema.get('reviews_per_month', False) 	
        calculated_host_listings_count = schema.get('calculated_host_listings_count', False) 	
        availability_365 = schema.get('availability_365', False) 	
        neighbourhood_group = schema.get('neighbourhood_group', False)
        
        data = ModelResidencias.query

        if name:
            data = data.filter_by(name=name)

        if host_id:
            data = data.filter_by(host_id=host_id)

        if host_name:
            data = data.filter_by(host_name=host_name)

        if neighbourhood:
            data = data.filter_by(neighbourhood=neighbourhood)

        if latitude:
            data = data.filter_by(latitude=latitude)

        if longitude:
            data = data.filter_by(longitude=longitude)

        if room_type:
            data = data.filter_by(room_type=room_type)

        if price:
            data = data.filter_by(price=price)

        if minimum_nights:
            data = data.filter_by(minimum_nights=minimum_nights)

        if number_of_reviews:
            data = data.filter_by(number_of_reviews=number_of_reviews)

        if last_review:
            data = data.filter_by(last_review=last_review)

        if reviews_per_month:
            data = data.filter_by(reviews_per_month=reviews_per_month)

        if calculated_host_listings_count:
            data = data.filter_by(calculated_host_listings_count=calculated_host_listings_count)

        if availability_365:
            data = data.filter_by(availability_365=availability_365)

        if neighbourhood_group:
            data = data.filter_by(neighbourhood_group=neighbourhood_group)


        return ResponseResidenciasSchema(many=True).dump(data.all())