Feature: confirm the comparison page works as expected

    Scenario: Display or get the comparison page
        Given we want to compare different sensors of the same type
		When  we click on the comparison link
		Then the comparison page opens