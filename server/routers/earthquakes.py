from fastapi import APIRouter, Request

router = APIRouter();

@router.get("/api/earthquakes")
def get_earthquakes(request: Request):
    """
    grabs the dataframe from the app state and returns a list of earthquake data.
     Returns:
        A list of dictionaries, each containing earthquake data such as id, magnitude, depth, location, and tsunami information.
    """
    df = request.app.state.df

    earthquakes = []
    for index, row in df.iterrows():
        earthquakes.append({
            "id": int(index) + 1,
            "magnitude": float(row['magnitude']),
            "depth": float(row['depth']),
            "latitude": float(row['latitude']),
            "longitude": float(row['longitude']),
            "year": int(row['Year']),
            "month": int(row['Month']),
            "isTsunami": bool(row['tsunami_boolean'])
        })  

    return earthquakes

