from fastapi import FastAPI
from pydantic import BaseModel
import folium

app = FastAPI()

class Location(BaseModel):
    lat: float
    lng: float

@app.post("/location")
def receive_location(loc: Location):
    m = folium.Map(location=[loc.lat, loc.lng], zoom_start=15)
    folium.Marker([loc.lat, loc.lng], popup="User Location").add_to(m)
    m.save("location.html")
    return {"status": "location saved"}
