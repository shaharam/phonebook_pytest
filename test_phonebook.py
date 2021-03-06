import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook():
    phonebook = Phonebook()
    yield phonebook
    phonebook.clear()


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert phonebook.names() == {"Bob"}


def test_phonebook_contains_all_names_in(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    phonebook.add("Bob", "1234")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
