# Builder Pattern Assignment: Custom Computer Builder
 
## Objective

Implement the Builder pattern to construct custom computer configurations with various components and specifications.

## Background

You're building a system for a computer shop that allows customers to configure custom PCs. A computer has many optional components and configurations, making the construction process complex. The Builder pattern will help separate the construction logic from the representation.

## Requirements

### Part 1: Basic Builder Implementation

Create a Computer class with the following attributes:
- cpu (required)
- ram (required, in GB)
- storage (required, in GB)
- gpu (optional)
- motherboard (optional)
- power_supply (optional, in watts)
- case (optional)
- cooling_system (optional)
- wifi_card (optional, boolean)
- bluetooth (optional, boolean)

#### Implement a ComputerBuilder class that:

- Provides methods to set each attribute
- Returns self from each method to enable method chaining
- Has a build() method that returns the completed Computer object
- Validates that required fields (cpu, ram, storage) are set before building

### Part 2: Director Class

Create a ComputerDirector class with pre-configured build methods:

- build_gaming_pc() - High-end gaming configuration
- build_office_pc() - Basic office work configuration
- build_workstation() - Professional workstation for content creation

Each method should accept a builder and configure it appropriately.

### Part 3: Bonus Challenge

Implement a second builder, ComputerSpecBuilder, that builds the same Computer objects but focuses on specifications rather than brand names (e.g., "8-core processor" instead of "Intel i7-9700K").

#### Constraints

- The Computer class should be immutable after construction
- Don't use a constructor with many parameters - that defeats the purpose of the Builder pattern
- Include a __str__ or __repr__ method on Computer for easy display

##### Example Usage

Your implementation should support usage like this:

```
python# Direct builder usage
builder = ComputerBuilder()
computer = (builder
    .set_cpu("Intel i9-13900K")
    .set_ram(32)
    .set_storage(1000)
    .set_gpu("NVIDIA RTX 4080")
    .set_wifi_card(True)
    .build())
```
##### Using director
```
director = ComputerDirector()
gaming_pc = director.build_gaming_pc(ComputerBuilder())
```

### Deliverables

Complete implementation of all classes

A demonstration script showing:
Manual building of a custom computer
Using the director to build all three preset configurations
Attempting to build without required fields (should raise an error)

### Testing Your Implementation

Make sure to test:
- Building computers with only required fields
- Building computers with all optional fields
- Method chaining works properly
- Director creates appropriate configurations
- Validation catches missing required fields

Good luck! This exercise will help you understand when and how to use the Builder pattern for objects with complex construction logic.