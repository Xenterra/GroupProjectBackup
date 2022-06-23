Feature: checking all sensor details
	
	Scenario: Get a list of all sensors in the system
		Given we want to view the list of sensors
		When we click the List link
		Then the page opens

	Scenario: Get details of one sensor
		Given I want to find out more details of one sensor in the system
		When I click the List link
		Then I click the More Details button  
		Then I go to the Sensor Details page (the Sensor Details page opens)
	
	Scenario: Get data collected by the sensor
		Given We want to query the data collected by the sensor
		When we use the list link
		Then display the information collected by the sensor