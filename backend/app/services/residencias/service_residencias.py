from flask import current_app, request

from backend.app.views.residencias.schema import ResponseResidenciasSchema, RequestLikeSchema
from backend.core.models.model_residencias import ModelResidencias


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class ServiceResidencias:

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    @staticmethod
    def list_residencias(**schema):
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


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


    @staticmethod
    def list_preco_medio(**schema):
        rooms = ['Entire home/apt', 'Private room', 'Shared room']
        data = []
        for room in rooms:
            query = ModelResidencias.query
            query = query.filter_by(neighbourhood_group=schema.get('neighbourhood_group'))
            temp_data = {
                'neighbourhood_group': schema.get('neighbourhood_group'),
                'room_type': room,
                'price' : 0.0
            }
            media = 0
            query = query.filter_by(room_type=room)
            if len(query.all()) > 0:
                for row in query:
                    media += float(row.price)
                temp_data['price'] = media / len(query.all())
                data.append(temp_data)

        return data


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


    @staticmethod
    def like(**schema):
        id = request.json['id']
        data = ModelResidencias.query.filter_by(id=id).first()
        data.like = True
        current_app.db.session.commit()
        return RequestLikeSchema().dump(data) 
            
