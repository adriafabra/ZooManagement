Feature: Delete Booking
    In order to delete a booking
    As a user
    I want to delete a booking I registered

    Background: There are registered users and a booking by one of them
        Given Exists a user "user1" with password "password"
        And Exists a user "user2" with password "password"
        And Exists booking registered by "user1"
            | number_of_visitors | sector     | date       | hour  | user_city | user_region | user_country | user_phone |
            | 23                 | Mountain   | 2022-06-28 | 13:00 | Lleida    | Catalonia   | Spain        | 621544896  |

    Scenario: Try to delete a booking but not logged in
        Given I'm not logged in
        When I try to delete a booking with date "2022-06-28" and hour "13:00"
        Then I'm redirected to the login form

    Scenario: Try to delete a booking but not the owner
        Given I login as user "user2" with password "password"
        When I try to delete a booking with date "2022-06-28" and hour "13:00"
        Then Server responds with page containing "403 Forbidden"

    Scenario: Delete owned booking
        Given I login as user "user1" with password "password"
        When I delete the booking with date "2022-06-28" and hour "13:00"
        Then I'm viewing the home page for "user1"
        And There are 0 bookings