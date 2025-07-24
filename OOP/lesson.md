# introduction :

![WhatsApp Image 2025-07-07 at 14 58 51_24195dcc](https://github.com/user-attachments/assets/3fc1766d-0a0c-4d06-a638-6eb709c5f44c)

The best example to understand what is an object is the chest example : we have so many pieces in the game , every piece have multiple variables related to it, like the position, the color, the state(dead or not), it would be a touph job to deal with all those variables related to all those pieces seperately, actually we need to deal with those pieces as a whole thing, a whole variable, a whole object !

The first sort of object and classes have appeared were structs of c language, afterwards we found out that this concept is still limited, like we cannot define a function in the struct, as we have seen in the chest example, the piece object need some special functions like move(), a function that would allow the object to move and adjust the position

So there it comes the role of the objects and oop : 

- the object is an instance of a class 
- the class is a template for the object

bishop class example :
- We gonna make bishop class in the chest game, so we will need two objects of this class, it means two bishops, Every bishop has its variables (color, position, state, etc)

# OOP essentials :

lets dive into the OOP 4 backbones: 

- Encapsulation 
- Abstraction 
- Inheritance 
- Polymorphism

### encapsulation :
why do we use encapsulation ? and how to implement it correctly ?
first of all, encapsulation is based on 2 types pf methods, Setter and getters methods :
setters for changing values and getters for getting and seeing values
- Setters : They deal with changing the data and properties of the class
- Getters : we are just getting/fetching  data from the classes
  So why i should do this whole process (get the data and then set it (modify it)) while i can just modify them directly,
  Lets get back to the bishop example, lets say we moved directly the bishop position, imagine the new position is a position reserved by your opponent or a
  position that results in your king checkmate, So i should have validation methods to allow the piece movement in legal and appropriate way
![WhatsApp Image 2025-07-07 at 16 14 48_29ac8ea5](https://github.com/user-attachments/assets/f4c0a3cb-1954-4fd3-b593-ea9c56fd52f8)

another example of setting the attribute values :
Without encapsulation: 
U.password="", and oops then we have an error, the password is none !!!! 
But with encapsulation, we assure that the value assigned to it is valide

With encaps : 

def setpassword(self, newpass):

if len(new_pass) >= 6:
  
  self.password = new_pass

else:
 
  print("Password too short!")

And of course we have also get method not mentioned here

- encapsulation vs no encapsulation :

Student1= Student(name="wessim", age=22, specialty=" computer science*)
 
Speciality =" software developing"

Print (student1.speciality) 

Result : software developing 

this is an example of how i have modified an object attribute, but as you see we haven't respected the encapsulation concept, so this is how we do it with encapsulation and you will understand it better

!! but its not supposed to easily access my objects attributes and modify them in this simple way, it breaks the encapsulation concept

Lets see how to respect encaps and how useful it is.

Its forbidden to directly access and modify attributes or even directly print them without any encapsulation, So, at first i need setters and getters functions (methods)
So this is how it would be to print and modify student.name with encapsulation

![WhatsApp Image 2025-07-11 at 10 54 23_1778da47](https://github.com/user-attachments/assets/dae4856a-e5ba-4064-a195-5325b98929bd)

These are the definition of getters and setters method

![WhatsApp Image 2025-07-11 at 10 55 35_0d1d807f](https://github.com/user-attachments/assets/15ff14d2-d21f-49bc-b648-512ea11f4e35)

And this is how we used them to print and modify




## related general informations : 
- Primitive data types are the type which stores simple and one value like int float boolean char etc.
- Classes are blue prints for objects, blue prints meaning the original or the parent version
