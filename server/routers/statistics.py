from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/api/statistics")
def get_statistics(request: Request):
    """
    grabs the dataframe from the app state and calculates basic statistics about the earthquake and tsunami data.
     Returns:
        A dictionary containing the total number of earthquakes, average magnitude, tsunamis, and tsunami rate.
    """
    df = request.app.state.df

    total_earthquakes = len(df)
    total_tsunamis = int(df['tsunami_boolean'].sum())
    tsunami_rate = round(total_tsunamis / total_earthquakes * 100, 1)
    average_magnitude = round(float(df['magnitude'].mean()), 2)

    return {
        "total_earthquakes": total_earthquakes,
        "total_tsunamis": total_tsunamis,
        "tsunami_rate": tsunami_rate,
        "average_magnitude": average_magnitude
    }