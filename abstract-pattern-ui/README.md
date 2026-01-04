# Abstract Factory Pattern Practice Assignment

## Assignment:
Cross-Platform UI Component Factory

## Objective: 
Create an abstract factory system that produces families of related UI components for different operating systems (Windows, macOS, and Linux).

## Requirements:
Your system should create two types of UI components:

- Buttons - with methods like render() and click()
- Checkboxes - with methods like render() and toggle()

Each operating system should have its own distinctive style for these components.

### What you need to implement:

#### Abstract Products:
- Button (abstract base class)
- Checkbox (abstract base class)

#### Concrete Products for each OS:

- WindowsButton, MacButton, LinuxButton
- WindowsCheckbox, MacCheckbox, LinuxCheckbox

#### Abstract Factory:
- UIFactory (abstract base class with methods create_button() and create_checkbox())

#### Concrete Factories:
- WindowsFactory
- MacFactory
- LinuxFactory

#### Client code that:
- Accepts a factory as a parameter
- Uses the factory to create a button and checkbox
- Calls render() on both components
- Demonstrates that it works with any factory without knowing the concrete classes

### Example Output:

=== Windows UI ===
[Windows Button] rendered
[Windows Checkbox] rendered

=== Mac UI ===
(Mac Button) rendered
(Mac Checkbox) rendered

=== Linux UI ===
{Linux Button} rendered
{Linux Checkbox} rendered

### Bonus Challenges:

Add a third component type (e.g., TextInput)

Add a fourth operating system variant

Implement a factory selector that chooses the appropriate factory based on a configuration string

Add validation to ensure all components from a factory are used together (preventing mixing Windows buttons with Mac checkboxes)

Good luck! This exercise will help you understand how Abstract Factory ensures families of related objects are created together consistently.