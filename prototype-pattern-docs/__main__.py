from documents.contract_prototype import Contract
from document_registry import DocumentRegistry

# Create a document registry instance
document_registry = DocumentRegistry()

# Create a test object based on the contract class
# We will use this to register an NDA document in the registry

nda = Contract()
nda.party_a = "Company"
nda.terms = "Don't talk about it"
nda.title = "Non-Disclosure Agreement"
nda.metadata = {"tag": "NDA"}

# Demonstrating adding the new document type to the registry
document_registry.add('NDA',nda.clone())

# Modifying the original NDA object to demonstrate that changes don't propagate to the new object
nda.party_a = "Testing"
nda.metadata = {"tag": "Modified"}

print("Original NDA:")
nda.display()

# Demonstrating gettinga clone of the document from the registry
nda2 = document_registry.get('NDA')

# Display the contents of the document
print ("Modified NDA:")
nda2.display()