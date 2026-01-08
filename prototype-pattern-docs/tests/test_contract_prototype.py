import pytest
from contract_prototype import Contract

class TestContract(): 

    def test_properties(self, basic_contract: Contract): 
        assert basic_contract.title == "Test Title"
        assert basic_contract.party_a == "Party A"
        assert basic_contract.party_b == "Party B"
        assert basic_contract.terms == "Terms"
        assert basic_contract.metadata == {"data1": "Test", "datum2": "Testing"}
        assert basic_contract.content == "Content"

    def test_clone(self, basic_contract): 
        clone = basic_contract.clone()
        # Verify clone is equivalent (same values)
        assert clone == basic_contract
        # Verify clone is a different object (not the same instance)
        assert clone is not basic_contract
