# PollingSite model represents the polling sites in the system
PollingSite:
  fields:
    name:
      type: CharField
      max_length: 255
      description: "The name of the polling site."
    
    address:
      type: TextField
      description: "The address of the polling site."
    
    state:
      type: CharField
      max_length: 100
      description: "The state where the polling site is located."
    
    county:
      type: CharField
      max_length: 100
      description: "The county where the polling site is located."
    
    city_or_town:
      type: CharField
      max_length: 100
      description: "The city or town where the polling site is located."
    
    contact_person:
      type: ForeignKey
      related_model: User
      null: true
      blank: true
      on_delete: SET_NULL
      description: "The contact person for the polling site."
    
    team_leader:
      type: ForeignKey
      related_model: User
      null: true
      blank: true
      on_delete: SET_NULL
      description: "The assigned team leader for the polling site."
    
    risk_assessment:
      type: OneToOneField
      related_model: Assessment
      null: true
      blank: true
      on_delete: SET_NULL
      description: "The risk assessment associated with the polling site."

# State model represents the states
State:
  fields:
    name:
      type: CharField
      max_length: 100
      unique: true
      description: "The name of the state."

# County model represents the counties within a state
County:
  fields:
    name:
      type: CharField
      max_length: 100
      description: "The name of the county."
    
    state:
      type: ForeignKey
      related_model: State
      on_delete: CASCADE
      description: "The state to which the county belongs."

# CityOrTown model represents the cities or towns within a county
CityOrTown:
  fields:
    name:
      type: CharField
      max_length: 100
      description: "The name of the city or town."
    
    county:
      type: ForeignKey
      related_model: County
      on_delete: CASCADE
      description: "The county to which the city or town belongs."