import pytest
from documents import Contract, AbsDocument

@pytest.fixture
def basic_contract(): 
    contract = Contract(); 
    contract.title = "Test Title"
    contract.party_a = "Party A"
    contract.party_b = "Party B"
    contract.terms = "Terms"
    contract.metadata = {"data1": "Test", "datum2": "Testing"}
    contract.content = "Content"
    return contract
    