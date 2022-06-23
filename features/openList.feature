Feature: checking all sensor details
	
	Scenario: Get a list of all sensors in the system
		Given we want to view the list of sensors
		When we click the List link
		Then the page opens

	Scenario: Get details of one sensor
		Given I want to find out more details of one sensor on the map.
		When I click one sensor pin on the map.
		Then I click the More Details link.  
		Then I go to the Sensor Details page. (the Sensor Details page opens)