import json
import requests
from flask import Flask

INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])

def get_incidents(unit_type):
  # create an empty list called 'incidents'
    incidents = []

  # use 'requests' to do a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL)

  # retrieve the JSON from the response
    info = response.json()
  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list
    for i in range(len(info['ElevatorIncidents'])):
      if unit_type.upper() == info['ElevatorIncidents'][i]['UnitType']:
        individual_incident = {}
        individual_incident = {'StationCode': info['ElevatorIncidents'][i]['StationCode'], 'StationName': info['ElevatorIncidents'][i]['StationName'], 'UnitType': info['ElevatorIncidents'][i]['UnitType'], 'UnitName': info['ElevatorIncidents'][i]['UnitName']}
        incidents.append(individual_incident)
  # return the list of incident dictionaries using json.dumps()
    readout = json.dumps(incidents)
    return(readout)

if __name__ == '__main__':
    app.run(debug=True)
