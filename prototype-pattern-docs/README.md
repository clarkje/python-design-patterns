# Prototype Pattern Assignment: Document Template System


## Objective
Create a document template system that uses the Prototype pattern to clone and customize various document types efficiently.

## Background

You're building a document generator for a company that frequently creates similar documents (contracts, invoices, reports). Instead of creating each document from scratch, you'll use prototypes that can be cloned and customized.

##Requirements

Implement a system with the following components:

### Abstract Prototype: 

Create a Document base class with:
Properties: title, content, metadata (dict), sections (list)
An abstract clone() method
A display() method to show the document details

### Concrete Prototypes: 

Implement at least three document types:
- Contract: 
  - Has additional fields like party_a, party_b, terms
- Invoice: 
  - Has fields like invoice_number, items (list of dicts), total
- Report: 
  - Has fields like author, date, data_points (list)

### Prototype Registry: 

Create a DocumentRegistry class that:

Stores prototype instances by name
Provides methods to register and retrieve (clone) prototypes
Handles both shallow and deep copy scenarios appropriately

### Customization: 

After cloning, demonstrate modifying the cloned documents without affecting the original prototypes

### Challenge Elements

- Implement deep copying correctly so that mutable objects (lists, dicts) aren't shared between clones
- Handle the case where nested objects within documents also need proper copying
- Create at least one document with a nested object (e.g., an Address class) to practice deep copying complexities

### Expected Output

Your program should demonstrate:
- Registering prototype documents in the registry
- Cloning documents from the registry
- Modifying cloned documents independently
- Showing that originals remain unchanged

### Bonus Challenges

- Implement both clone() and deep_clone() methods to show the difference
- Add a method to compare two documents and show what's different
- Implement a merge() method that combines sections from multiple document prototypes

This assignment will help you understand when and why to use Prototype pattern, especially for complex object initialization and when you need many similar but customized instances.