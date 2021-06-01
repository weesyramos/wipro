from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class ModelResidencias(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)	
    host_id	 = db.Column(db.String(255), nullable=False)
    host_name = db.Column(db.String(255), nullable=False)	
    neighbourhood = db.Column(db.String(255), nullable=False)	
    latitude = db.Column(db.String(255), nullable=False)	
    longitude = db.Column(db.String(255), nullable=False)	
    room_type = db.Column(db.String(255), nullable=False)	
    price = db.Column(db.String(255), nullable=False)	
    minimum_nights = db.Column(db.String(255), nullable=False)	
    number_of_reviews = db.Column(db.String(255), nullable=False)	
    last_review = db.Column(db.String(255), nullable=False)	
    reviews_per_month = db.Column(db.String(255), nullable=False)	
    calculated_host_listings_count = db.Column(db.String(255), nullable=False)	
    availability_365 = db.Column(db.String(255), nullable=False)	
    neighbourhood_group = db.Column(db.String(255), nullable=False)
    like = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return '<Nme %r>' % self.name