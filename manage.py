import pandas as pd

from backend import create_app, app
from backend import settings
from flask_script import Manager


app = create_app()
manager = Manager(app)


@manager.command
def run_bases():
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

    new_df.to_csv('bases/aqui.csv', index = False)

    


if __name__ == "__main__":
    port = settings.PORT
    manager.run()
    app.run(debug=True, host='0.0.0.0', port=port)


    # id	
    # name	
    # host_id	
    # host_name	
    # neighbourhood	
    # latitude	
    # longitude	
    # room_type	
    # price	
    # minimum_nights	
    # number_of_reviews	
    # last_review	
    # reviews_per_month	
    # calculated_host_listings_count	
    # availability_365	
    # neighbourhood_group
