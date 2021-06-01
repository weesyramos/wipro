import pandas as pd

from flask import current_app
from flask_script import Manager

from backend import create_app, app
from backend import settings
from backend.core.models.model_residencias import ModelResidencias

app = create_app()
manager = Manager(app)


@manager.command
def run_bases():
    # MANIPULA E CRIA .CSV
    NAMES_GROUP = ['Brooklyn', 'Manhattan', 'Queens', 'Staten Island']

    df_airbnb = pd.read_csv('bases/airbnb_ny_2019.csv',encoding='utf-8', delimiter=',')
    df_airbnb = df_airbnb.drop_duplicates()
    df_airbnb = df_airbnb.dropna()

    df_vizinhanca = pd.read_csv('bases/mapeamento_vizinhanca.csv',encoding='utf-8', delimiter=',')
    df_vizinhanca = df_vizinhanca.drop_duplicates()
    df_vizinhanca = df_vizinhanca.dropna()

    new_df = pd.merge(df_airbnb, df_vizinhanca,  how='left', left_on='neighbourhood', right_on='vizinhanca')
    new_df.rename(columns = {'vizinhanca_grupo':'neighbourhood_group'}, inplace = True)
    del new_df['vizinhanca']

    filter_neighbourhood_group = lambda x: x in NAMES_GROUP
    new_df = new_df[new_df['neighbourhood_group'].map(filter_neighbourhood_group)]

    new_df.to_csv('bases/residencias.csv', index = False)
    _commit_bases_csv_bd(new_df)

def _commit_bases_csv_bd(df):
    # ITERA SOBRE O DATA FRAME MANIPULADO E PERSISTE NO DB
    for index, row in df.iterrows():
        data = ModelResidencias(
            name = row['name'],
            host_id = row['host_id'],	
            host_name = row['host_name'],	
            neighbourhood = row['neighbourhood'],	
            latitude = row['latitude'],
            longitude = row['longitude'],	
            room_type = row['room_type'],	
            price = row['price'],	
            minimum_nights = row['minimum_nights'],	
            number_of_reviews = row['number_of_reviews'],	
            last_review = row['last_review'],	
            reviews_per_month = row['reviews_per_month'],	
            calculated_host_listings_count = row['calculated_host_listings_count'],	
            availability_365 = row['availability_365'],	
            neighbourhood_group = row['neighbourhood_group']
        )
        current_app.db.session.add(data)
        current_app.db.session.commit()


if __name__ == "__main__":
    port = settings.PORT
    manager.run()
    app.run(debug=True, host='0.0.0.0', port=port)