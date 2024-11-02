from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):

    # ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalator').status_code
        # assert that the response code of 'incidents/escalators returns a 200 code
        self.assertEqual(escalator_response, 200)
        elevator_response = app.test_client().get('/incidents/elevator').status_code
        # assert that the response code of 'incidents/elevators returns a 200 code
        self.assertEqual(elevator_response, 200)

################################################################################

    # ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get('/incidents/escalator')
        json_response = json.loads(response.data.decode())
        # for each incident in the JSON response assert that each of the required fields
        # are present in the response
        x = 0
        for i in range(len(json_response)):
            if required_fields == list(json_response[i].keys()):
                x += 0
            else:
                x += 1
        self.assertEqual(x, 0)
################################################################################

    # ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalator')
        json_response = json.loads(response.data.decode())
        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        x = 0
        for i in range(len(json_response)):
            if json_response[i]['UnitType'] == 'ESCALATOR':
                x+=0
            else:
                x+=1
        self.assertEqual(x, 0)
################################################################################

    # ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevator')
        json_response = json.loads(response.data.decode())
        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        x = 0
        for i in range(len(json_response)):
            if json_response[i]['UnitType'] == 'ELEVATOR':
                x+=0
            else:
                x+=1
        self.assertEqual(x, 0)
################################################################################

if __name__ == "__main__":
    unittest.main()