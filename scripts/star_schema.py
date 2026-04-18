import pandas as pd

# Load data
df = pd.read_csv("data/processed/final_data.csv")

# CREATE DIMENSIONS

# dim_user
dim_user = df[['user_id']].drop_duplicates()

# dim_route
dim_route = df[['route']].drop_duplicates().reset_index(drop=True)
dim_route['route_id'] = dim_route.index + 1

# dim_city
dim_city = df[['city']].drop_duplicates().reset_index(drop=True)
dim_city['city_id'] = dim_city.index + 1

# dim_vehicle
dim_vehicle = df[['vehicle_type']].drop_duplicates().reset_index(drop=True)
dim_vehicle['vehicle_id'] = dim_vehicle.index + 1

# CREATE FACT TABLE

# Merge IDs into main df
fact = df.merge(dim_route, on='route') \
         .merge(dim_city, on='city') \
         .merge(dim_vehicle, on='vehicle_type')

fact_table = fact[[
    'ticket_id',
    'user_id',
    'route_id',
    'city_id',
    'vehicle_id',
    'price',
    'price_norm',
    'price_category'
]]

# SAVE FILES

dim_user.to_csv("data/star/dim_user.csv", index=False)
dim_route.to_csv("data/star/dim_route.csv", index=False)
dim_city.to_csv("data/star/dim_city.csv", index=False)
dim_vehicle.to_csv("data/star/dim_vehicle.csv", index=False)
fact_table.to_csv("data/star/fact_tickets.csv", index=False)

print("Star Schema Created Successfully!")