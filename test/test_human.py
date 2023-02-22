from src.human import Human

def test_get_fullname():
    person = Human(82, 'man', 'Ole', 'Nydhal', 175, 'grey')
    expected_fullname = 'Ole Nydhal'
    assert person.get_full_name() == expected_fullname

def test_age_in_days():
    person = Human(82, 'man', 'Ole', 'Nydhal', 175, 'grey')
    expected_age = 29930
    assert person._age_in_days() == expected_age
