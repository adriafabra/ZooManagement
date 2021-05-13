Feature: Edit Booking
    In order to modify a booking
    As a user
    I want to edit a booking I registered

    Background: There are registered users and a booking by one of them
        Given Exists a user "user1" with password "password"
        And Exists a user "user2" with password "password"
        And Exists booking registered by "user1"
            | number_of_visitors | sector     | date       | hour  | user_city | user_region | user_country | user_phone |
            | 23                 | Mountain   | 2022-06-28 | 13:00 | Lleida    | Catalonia   | Spain        | 621544896  |

    Scenario: Edit owned booking 
        Given I login as user "user1" with password "password"
        When I edit the booking with date "2022-06-28" and hour "13:00"
            | number_of_visitors  |
            | 34                  |
        Then I'm viewing the details page for booking by "user1"
            | number_of_visitors | sector     | date       | hour  | user_city | user_region | user_country | user_phone |
            | 34                 | Mountain   | 2022-06-28 | 13:00 | Lleida    | Catalonia   | Spain        | 621544896  |
        And There are 1 bookings

    Scenario: Try to edit a booking but not logged in
        Given I'm not logged in
        When I try to edit a booking with date "2022-06-28" and hour "13:00"
        Then I'm redirected to the login form

    Scenario: Try to edit a booking but not the owner
        Given I login as user "user2" with password "password"
        When I try to edit a booking with date "2022-06-28" and hour "13:00"
        Then Server responds with page containing "403 Forbidden"