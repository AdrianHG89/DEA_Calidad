Feature: Paginas Web estaticas en django


	Scenario: Help have content
		Given I access the url "/help/"
		Then I see the header "AYUDA"

	Scenario: About have content
		Given I access the url "/about/"
		Then I see the header "SOBRE NOSOTROS"

	Scenario: Contact have content
		Given I access the url "/contact/"
		Then I see the header "Contacto"

	Scenario: Contact have index
		Given I access the url "/index/"
		Then I see the header "RAVEN"