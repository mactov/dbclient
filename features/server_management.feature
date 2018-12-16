Feature: Server Management

  Scenario: List all servers
   Given The localhost and db.iablaka.com are in the server list
    When I list them
    Then I get this [{"server": "localhost"}, {"server": "db.iablaka.com"}]
