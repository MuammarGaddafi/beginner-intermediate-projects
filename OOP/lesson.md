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


### the secret and the utility of using encapsulation :

I see no utility in using private attributes and then changing them and accessing them with getters and setters, if i gonna change them i simply change them in the common way student.age = .... Why am i doing all these stuffs, i see nothing special in encapsulation, i dont see why am i protecting the attributes and from who


My answer : yeah, i feel you, maybe encapsulation seems useless and you don't know for which cases and users is it made for, you can't see the encapsulation real magic with those simple examples where it could be useless, but stay with me over this example and you will understand every point of it

Encapsulation utility appears when you work with complex projects and especially with co workers and when you fix or work on an already existing code in a company, see this copilot example and explanation

![WhatsApp Image 2025-07-11 at 11 50 12_26728fa7](https://github.com/user-attachments/assets/b70d1bf3-17e2-4588-a185-41ab6df01a28)

![WhatsApp Image 2025-07-11 at 11 50 26_3a8477f1](https://github.com/user-attachments/assets/091cbed8-2ae7-49e7-ab9d-bd26ba8009f7)

![WhatsApp Image 2025-07-11 at 11 50 46_667ed73e](https://github.com/user-attachments/assets/cf877cc7-9ea4-4d7f-9358-bec60ac36f6d)

So the conclusion encapsulation prevent and return messages when changes are not valid and the messages and the code behaviour would clarify to the person who work on it for the first time all what he need to understand and the code process and mechanism, not just that, it would make things easier even for your future self when you get back to the code and trying to work on it and certainly you have forgotten bunch of things about it so it would be much more helpful to cope with it

![WhatsApp Image 2025-07-11 at 12 15 50_6e58ddaf](https://github.com/user-attachments/assets/6bf73d8a-ea4e-4b51-b070-1389b398508b)

When It’s Overkill ?

- You’re doing a quick script or solo project
- The attribute doesn't require validation
- No other code depends on your class


# Abstraction :

abstraction is actually needed to create a class which contains methods and attributes, called abstracted class that we cant make instances of it and use its features and abstracted methods, so its created not to give us instances since we cannot make objects from abstracted classes but it's created to define how children classes would behave (any abstract class should have children classes that inherit all the class properties)
- while working in a company, you may have a task of fixing or working on specific class, abstraction allow you to work on this class without worrying about the other classes and their roles or even knowing what they are, you only focus on your task it couldn't be affected by other classes

### abstraction syntax and implementation : 



# Inheritance : 

![WhatsApp Image 2025-07-08 at 23 33 33_d77c683a](https://github.com/user-attachments/assets/ed01db57-89b7-4bb6-8c7b-f18c161ce61c)

As we see, sometimes we get many common attributes between this two classes, and we know the famous concept of IT. World : do not repeat 


So the best solution is to make new class called person then the student and teacher classes would inherit those attributes from this class


The person is called the parent class

![WhatsApp Image 2025-07-08 at 23 36 10_94489065](https://github.com/user-attachments/assets/689d73f7-b9d8-4632-8ef6-a093a5c0aaec)



# Polymorphism : 

poly means multiple and morphism means the shape it takes : so it means that a thing could take more than shape and aspect
So here in oop it means that the method could behave and act in multiple ways
- polymorphism devides into two essentials : over loading and over riding

Overloading vs overriding simply : 
The name speaks for itself :over loading is loading the method over and over with different number and types of arguments
Over riding is riding the method over and over with different behaviour and needs every time when the method is inherited 


Overloading is the same method but can take multiple and different arguments in every call 

Over riding :related to inheritance,  when a subclass redefine the **same** method **inherited** from the parent class to change its behavior 
Thats all

![WhatsApp Image 2025-07-12 at 13 21 45_e9c8cebf](https://github.com/user-attachments/assets/000fda02-daac-4c9f-a97f-da9226ac41dc)

utility : 
If we don't use polymorphism, in many cases we gonna go through a serious trouble, bcz working on real life projects would be intensely complexe, if we use new method for every need while the parameters are different or the behaviour is slightly different, we will make new method every time like sum1() which accepts 2 integers, sum2() which accept two floats, sum3() which accepts 3 integers ...... Until we end up using even 32 different sum method, which is not practical, so with polymorphism we may use only one method with different behaviours or different arguments

### how to implement them :
1) over loading :
   we will take a method called  sum() as an example 

   First time its sum(int x , int y)
   
   Second time used its sum(int x int y int z)
   
   Third time : sum (float x , float y)

   so we used the same method with same behaviour but we change the number and type of arguments without changing the code of the method





# OOP SYNTAX : 






## related general informations : 
- Primitive data types are the type which stores simple and one value like int float boolean char etc.
- Classes are blue prints for objects, blue prints meaning the original or the parent version
