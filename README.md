This is one of the product ideas I wanted to explore (a job board), but more importantly, to explore some architecture ideas I've had.
![Domain_Action_driven_architecture](https://user-images.githubusercontent.com/9606801/140606175-703acd50-dff3-4958-a7d8-29384279e480.jpg)

The idea is - as I understand - a mix between hexagonal and domain-driven architectures.

# Entities & Actions - aka the Domain
The two most important constructs: entities and actions. 
An entity is a business concept, like an account, a bank card, or a doorknob if that's the product of the company.

Actions are what the business usually have to/want to do with entities. Like open an account, register a bank card, or prepare an invoice for a doorknob.

The only restraint this domain should have is the language itself, it shouldn't care about the DB you're using (if any!), or whether your application is a web application, a mainframe program, or whatever.

# Adapters

Then there comes repositories, which should give you a basic CRUD interface over entities. 
In here you inject a kind of object that will manage persistence, like a class instance who knows how to speak with the database, or read/write from CSV.

# Renderers

Finally there are renderers, which are web frameworks, terminal applications, whatever. At this stage you'll need to worry about problems specific to the application's type (think of authentication in webapps for example). Other than these, this layer should mostly be configuration, like setting up a route to a perform a certain domain action.


## Lessons learned

This was a fun exercise, and I definitely see value in this approach, it's very lean, and uses very few dependencies compared to other solutions - *BUT* Django (to remain in the Python realm) beats this in terms of productivity and time to launch, while still offering this architecture as an evolutionary next step once the product is deemed profitable, and needs to separate domain specific actions/events from the framework.
