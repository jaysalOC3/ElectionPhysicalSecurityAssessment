# PollingSiteForm for creating and updating polling sites
## PollingSiteForm
### Fields
- **name**
  - Type: CharField
  - Widget: TextInput
  - Description: The name of the polling site.
- **address**
  - Type: CharField
  - Widget: Textarea
  - Description: The address of the polling site.
- **state**
  - Type: ModelChoiceField
  - Queryset: State.objects.all()
  - Description: The state where the polling site is located.
- **county**
  - Type: ModelChoiceField
  - Queryset: County.objects.all()
  - Description: The county where the polling site is located.
- **city_or_town**
  - Type: ModelChoiceField
  - Queryset: CityOrTown.objects.all()
  - Description: The city or town where the polling site is located.
- **contact_person**
  - Type: ModelChoiceField
  - Queryset: User.objects.all()
  - Required: false
  - Description: The contact person for the polling site.
- **team_leader**
  - Type: ModelChoiceField
  - Queryset: User.objects.all()
  - Required: false
  - Description: The assigned team leader for the polling site.
- **site_type**
  - Type: ChoiceField
  - Choices: PollingSite.SITE_TYPE_CHOICES
  - Description: The type of polling site.