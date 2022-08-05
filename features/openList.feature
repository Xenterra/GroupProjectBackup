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

	Scenario: Get details of one sensor from the map page
		Given I want to find out more details of one sensor from the map
		When I click a map marker
		Then I click the More Details button in the popup 
		Then I go to the Sensor Details page of that sensor