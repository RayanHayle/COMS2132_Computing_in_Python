#kbest.py 25 points
import requests
import time
from datetime import datetime
from  kbest import KBestCounter
class Earthquake:

  def __init__(self, json):
    props = json['properties']
    self.time = float(props['time']) / 1000
    self.mag = float(props['mag'])
    self.place = props['place']
    coord = json['geometry']['coordinates']
    self.latitude, self.longitude, self.depth = float(coord[0]), float(coord[1]), float(coord[2])

  def __repr__(self): 
    time = str(datetime.fromtimestamp(self.time)) 
    return f"{time} -- {self.mag} {self.place}"  
   
  #__hash__(self)   __eq__(self) _gt__  __lt__, and __eq__ 
  def __hash__(self):
    return hash((self.time, self.mag, self.place))

  #class comparable by magnitude by implementing appropriate
  def __gt__(self, other):
          return self.mag > other.mag

  def __lt__(self, other):
          return self.mag < other.mag

  def __eq__(self, other):
          return self.mag == other.mag


def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        json_quake_list =  data["features"]
        return [Earthquake(json_quake) for json_quake in json_quake_list]
    else:
        print("Error fetching data:", response.status_code)
        return []



def print_data():
    while True:
        earthquakes = fetch_earthquake_data()
        for q in earthquakes: 
          print(q)
        print()
        time.sleep(60)

def print_new_quakes():
     # Replace for part a) 
     #You will need to keep track of the earthquakes seen so far in a python set.
     Seen_Earthquakes = set()
     while True:
         earthquakes = fetch_earthquake_data()

         for item in  earthquakes:
             if item not in Seen_Earthquakes:
                 print(item)
                 Seen_Earthquakes.add(item) #not append --> its set not linkedlist 
         print()
         time.sleep(60)
           

def print_k_largest(k=3):
    # Replace for part b)

  Seen_Earthquakes = set()
  k_best_counter = KBestCounter(k)
  while True:
      earthquakes = fetch_earthquake_data()
      for item in earthquakes:
          if item not in Seen_Earthquakes:
              k_best_counter.count(item)
              Seen_Earthquakes.add(item)
      print(f"--- {datetime.now()} --- largest earthquakes:")
      for quake in k_best_counter.kbest():
          print(quake)

      print() 
      time.sleep(60)


if __name__ == "__main__":

    # only one of the following three functions shoudl be called at a time
    #print_data()
    '''
    2025-04-18 19:22:02.430000 -- 0.86 2 km ENE of The Geysers, CA
    2025-04-18 19:09:00.919000 -- 1.3 31 km WSW of Petersville, Alaska
    2025-04-18 19:06:51.062000 -- 1.3 59 km WSW of Salamatof, Alaska
    2025-04-18 18:57:28.500000 -- 1.37 11 km WNW of Borrego Springs, CA
  '''
    #print_new_quakes() 
    '''
    2025-04-18 19:53:23.320000 -- 1.17 15 km SSE of Borrego Springs, CA
    2025-04-18 19:22:02.430000 -- 0.86 2 km ENE of The Geysers, CA
    2025-04-18 19:09:00.919000 -- 1.3 31 km WSW of Petersville, Alaska
    2025-04-18 19:06:51.062000 -- 1.3 59 km WSW of Salamatof, Alaska
    2025-04-18 18:57:28.500000 -- 1.37 11 km WNW of Borrego Springs, CA

    '''


    print_k_largest(3) 
    '''--- 2025-04-18 19:59:34.770809 --- largest earthquakes:
      2025-04-18 19:06:51.062000 -- 1.3 59 km WSW of Salamatof, Alaska
      2025-04-18 19:09:00.919000 -- 1.3 31 km WSW of Petersville, Alaska
      2025-04-18 19:22:02.430000 -- 0.86 2 km ENE of The Geysers, CA
      '''
