# PollingSite model represents the polling sites in the system
## PollingSite
### Fields
- **name**
  - Type: CharField
  - Max Length: 255
  - Description: The name of the polling site.
- **address**
  - Type: TextField
  - Description: The address of the polling site.
- **state**
  - Type: CharField
  - Max Length: 100
  - Description: The state where the polling site is located.
- **county**
  - Type: CharField
  - Max Length: 100
  - Description: The county where the polling site is located.
- **city_or_town**
  - Type: CharField
  - Max Length: 100
  - Description: The city or town where the polling site is located.
- **contact_person**
  - Type: ForeignKey
  - Related Model: User
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The contact person for the polling site.
- **team_leader**
  - Type: ForeignKey
  - Related Model: User
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The assigned team leader for the polling site.
- **risk_assessment**
  - Type: OneToOneField
  - Related Model: Assessment
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The risk assessment associated with the polling site.

# State model represents the states
## State
### Fields
- **name**
  - Type: CharField
  - Max Length: 100
  - Unique: true
  - Description: The name of the state.

# County model represents the counties within a state
## County
### Fields
- **name**
  - Type: CharField
  - Max Length: 100
  - Description: The name of the county.
- **state**
  - Type: ForeignKey
  - Related Model: State
  - On Delete: CASCADE
  - Description: The state to which the county belongs.

# CityOrTown model represents the cities or towns within a county
## CityOrTown
### Fields
- **name**
  - Type: CharField
  - Max Length: 100
  - Description: The name of the city or town.
- **county**
  - Type: ForeignKey
  - Related Model: County
  - On Delete: CASCADE
  - Description: The county to which the city or town belongs.