Feature: Book Tour
    In order to register a zoo tour
    As a user
    I want to book a tour together with its number of visitors, sectors to visit, date and hour

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Register a booking
        Given I login as user "user" with password "password"
        When I book a tour
            | number_of_visitors | sector     | date       | hour  |
            | 12                 | 1          | 2022-05-28 | 10:00 |
        Then I'm viewing the details page for booking by "user"
            | number_of_visitors | sector     | date       | hour  |
            | 12                 | 1          | 2022-05-28 | 10:00 |
        And There are 1 bookings

    Scenario: Try to book a vist but not logged in
        Given I'm not logged in
        When I try to access booking page
        Then I'm redirected to the login form
        And There are 0 bookings