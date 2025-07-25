# introduction :

oop is a whole new way and  methodology of concepting and writing codes, it is the step right above the procedural programming, say good bye to procedural coding since it has its own utility and made our life easier in solving many problem but it comes to a limit where it cannot be pushed beyond it, so we need a new sort of programming to tackle more complexe solutions : 

Which is OOP, so its normal if you come across some new stuffs that may seem weird and obscure as they are so different to known concepts we learned in procedural programming


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

# encapsulation :
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

### implementation of private attributes for encapsulation : 

private attributes are attributes cannot be modified and shown and implement acts on it directly and easily : 
When the attribute is private, example : 

Self.__name 

Student1 is an object of student class 

When you write print(student1.name) it will give you an error because of undefined and unexisting name attribute 

When you write print(student1.__name), it will also give you an error, because private attribute cannot be given and accessed directly 

If you write Student1.name="ahmed" 
This is not considered as name attribute modifying, it will be considered as if you created a new attribute to the object student1 and assigned to it "ahmed", therefore if you write print(student1.name) it will print ahmed not an error, because you asked to print the newly created attribute called name, its different to the private attribute __name

so we use the getters and setters that allow us to get and modify those private attributes
the setters and getters syntax to deal with those private attributes :

<img width="970" height="366" alt="image" src="https://github.com/user-attachments/assets/20b8a426-ce30-47f0-a46e-9a6e0b8574d0" />

as we see we made private attributes and defined methods to get and set those private attributes so we prevented direct access to them




# Abstraction :

An abstract class is a class that cannot be instantiated on its own, meant to be subclassed (a parent class)

abstraction is actually needed to create a class which contains methods and attributes, called abstracted class that we cant make instances of it and use its features and abstracted methods, so its created not to give us instances since we cannot make objects from abstracted classes but it's created to define how children classes would behave (any abstract class should have children classes that inherit all the class properties)
- while working in a company, you may have a task of fixing or working on specific class, abstraction allow you to work on this class without worrying about the other classes and their roles or even knowing what they are, you only focus on your task it couldn't be affected by other classes
so  you need children classes to complete the job, so abstract classes are something like incomplete classes, we cannot create objects directly from incomplete classes

They can contain abstract methods that require children to inherit inheritedthose abstracrt methods, every abstract method created should be inherited otherwise it will rise an error

### abstraction syntax and implementation : 

Follow me with this example to understand how to use abstraction
We should import ABC class from abc libary
Then, we create the abstract parent class which would inherit from ABC class, Abstraction is used for classes neither you want  to create objects from it nor other programmers, so you wanna keep it abstracted, used only for defining the behaviour of the children classes
Any children class should inherit all the abstract methods, otherwise it would produce an error

![WhatsApp Image 2025-07-12 at 14 07 09_943bdcc2](https://github.com/user-attachments/assets/93dbe73c-a40f-4835-9d28-f1e32fa82ce4)

![WhatsApp Image 2025-07-12 at 14 08 04_46f191e9](https://github.com/user-attachments/assets/a273bc3f-0ca2-43f5-9f87-6e293cb4fced)

As you see this has produced an error because we are not allowed to create vehicle object since vehicle is abstracted class

![WhatsApp Image 2025-07-12 at 14 14 33_efbb5519](https://github.com/user-attachments/assets/fc65f0b5-c7e1-4a0b-a9de-6a76e882bb7f)

We created car class inherited from vehicle class, and we implemented the astracted methods all, so when we do car.go() it prints the appropriate message (we over rided the method in every new children class)

![WhatsApp Image 2025-07-12 at 14 17 25_8ed5371a](https://github.com/user-attachments/assets/2b44d597-7657-4505-b8f5-8d17d54cbdad)





# Inheritance : 

![WhatsApp Image 2025-07-08 at 23 33 33_d77c683a](https://github.com/user-attachments/assets/ed01db57-89b7-4bb6-8c7b-f18c161ce61c)

As we see, sometimes we get many common attributes between this two classes, and we know the famous concept of IT. World : do not repeat 


So the best solution is to make new class called person then the student and teacher classes would inherit those attributes from this class


The person is called the parent class

![WhatsApp Image 2025-07-08 at 23 36 10_94489065](https://github.com/user-attachments/assets/689d73f7-b9d8-4632-8ef6-a093a5c0aaec)

this is what child clas inherit from its parent class, almost every thing (instance methods, class attributes and methods, object attributes with some special syntax to fulfill it)

<img width="880" height="716" alt="image" src="https://github.com/user-attachments/assets/03427e0c-510d-4033-8e2f-5b9876b5dbb0" />




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

   !!! implementation of the over loading to make the method adapt to different and multiple arguments its a little bit tricky in python because direct over loading in python is not supported, so we have two options : adjusting the method to fit to multiple arguments, or make the method accept whatever argument with *arg

    adjusting the method to multiple args :

   ![WhatsApp Image 2025-07-09 at 00 22 11_247b568d](https://github.com/user-attachments/assets/22313fff-630f-4df7-bdd1-eee462dab073)

   difference between over loading between python and other languages :

   <img width="618" height="542" alt="image" src="https://github.com/user-attachments/assets/5ab4ecc9-34fe-4d20-a818-635283b3aa43" />

   ![WhatsApp Image 2025-07-14 at 19 31 34_6f889fce](https://github.com/user-attachments/assets/7df0b6b3-9320-47b6-9de5-b813acce991f)


We can even over ride dunders functions since they are considered inherited to all classes by default 
like in this example we gonna over ride the dunder function in this class, we gonna modify the way it returns the string result :

![WhatsApp Image 2025-07-12 at 14 48 33_113ae8f3](https://github.com/user-attachments/assets/4dcba95a-4971-4a1e-94cc-bef98f749b66)



# OOP SYNTAX : 

we usually use the dunder function init (dunder functions are inherited by default to any class in python), its a method make the initializing called automaticaly to fill the object attributes when its created 
if we dont define init method in the class the objects would be created when you call the class constructor but they would be empty without any attribute, so init is a method that automatically initialize the object with its attributes when its created 

so Its written with double undescore so that python interpretes it as a specifc method that blongs to the dunders and run automatically to create and initialize the object, without double score python would consider it as a common method created by the programmer, and won't run it automatically and wouldn't have sense

the init take self as a fixed argument which acts as the instances of the class
any attribute in the init method should be filled otherwise it would produce an error, if you want a default value for an attribute, you give it to the attribute when you give it as an argument for the init method : __ init __ ( self , state , number of children = 0 ) so if number of children is not filled it would have 0 as value since it is its default value

- anything (attributes) defined out of the init method, is called class attribute which would be given to any object created from that class directly (and class attributes should have assigned values)

When you want to access class attributes, like for example we have a class attribute called number of objects that is a value that increment every time we create an object of the class, you access it through the class name : calss.number_of_objects, and you can also access it through any object of the class and would show the same value whatever is the object, but for more clarity its better to access it with the class name


# Methods : 

there are 4 main types of methods

### instance methods : 

instance methods are the normal and the common methods
instance methods could be used on any object from whatever class and in any context (only if the method take self as an argument meaning it is related to class objects)

### class methods : 

- Class methods take only a class as an attribute, it couldn't take self or any thing related to the objects, it only take a class as an attribute so it can modify and access only things related to the class, like class attributes

<img width="688" height="526" alt="image" src="https://github.com/user-attachments/assets/01dfdaee-64bb-49a3-bfef-3b2bb5b97b93" />

this is an example of how we used and called the class method, it can take every thing of the cls (reference to the class) that does not belong to the object 

see in the general informations below how we used class methods for creating new instances from the class : 

So, one of the main utility of class method is creating objects in different way and with specific customization, this is so useful especially we cannot make more than one constructor (initialization ) method which is init, but with this trick now we can

diving deeper into it : 

![WhatsApp Image 2025-07-11 at 14 26 01_003ccca3](https://github.com/user-attachments/assets/4d802632-2c2e-4c08-83e2-4faea7a7275d)

![WhatsApp Image 2025-07-11 at 14 26 12_c4cd0b48](https://github.com/user-attachments/assets/d671fb5a-e556-47a9-a339-64265ad33e32)

![WhatsApp Image 2025-07-11 at 14 26 25_3fdb8441](https://github.com/user-attachments/assets/bb615140-0525-4bf7-a5d9-b2ba975bc68c)

another example on how cls methods are useful for customized object creation :

![WhatsApp Image 2025-07-11 at 16 12 42_772c868a](https://github.com/user-attachments/assets/47ed6eaf-c272-4e96-8e29-7787726c3a22)

As you see we created a pizza class, its objects would take only one attribute called ingredients which is a list of ingredients

If we want create specific type of this objects that its ingredients are well defined, as you see in the example, i made two class methods that help me to create pizza object that would be margherita and object that i want it vegetarian, and those two types of pizza i want them with well defined ingredients, so i made two class methods veg() and margherita() that don't take any argument, when i call them while creating a new pizza object they would create them as the wanted type : 

Example 

Pizza1=Pizza.veg() 

It would create a pizza object with those ingredients 

more ideas about it :

![WhatsApp Image 2025-07-11 at 16 31 23_28ba138a](https://github.com/user-attachments/assets/d2e0bd93-690d-4740-9476-d79c346b5bff)

Polymorphism object creation is what we saw in veg and margherita example

- Cls is referring to the class which is called, not necessarily calling the class where the method is created in 

Because in case like inheritance, the cls call the class which inherited the method from other class : like that :

![WhatsApp Image 2025-07-11 at 16 34 18_855e1760](https://github.com/user-attachments/assets/e050223a-0b14-4d9a-8cae-6676059d5f8a)

modifying class behaviour throught polymorphism :

![WhatsApp Image 2025-07-11 at 23 19 35_f5530815](https://github.com/user-attachments/assets/5dc2d48f-8f7e-4719-ba86-e35b8fc5c8aa)

![WhatsApp Image 2025-07-11 at 23 19 50_d136499b](https://github.com/user-attachments/assets/900700e1-d518-4696-9987-cf18a7257e52)





![WhatsApp Image 2025-07-11 at 16 31 42_eb8d6b95](https://github.com/user-attachments/assets/47a22346-a2e5-43da-bf51-738cf6c00fd9)


### abstract methods : 

we have seen it in the abstraction part


### static methods : 

Static methods : they don't take neither class as a parameter nor an object (self) 

But they can take arguments other than that
static methods could be used by any object from any class since they are not related to the class made in because doesnt take self (which is the object of the class reference) as a parameter

![WhatsApp Image 2025-07-12 at 15 03 28_0c8e3584](https://github.com/user-attachments/assets/590fc503-eeb5-4047-8012-ff76b0577654)

![WhatsApp Image 2025-07-12 at 15 11 48_806cdd31](https://github.com/user-attachments/assets/767292a2-7e5d-4521-84e9-b95d395d9348)

![WhatsApp Image 2025-07-12 at 15 15 53_d6dada02](https://github.com/user-attachments/assets/90a39890-29f0-49e9-820c-bc9f2e55fa70)


# important notes : 

1) You can have two methods with the same name but they shouldn't be in the same class otherwise one of them would over writes the other 
(This is not called over riding because they are not considered the same method, they are different methods despite same name since they are different classes python would interprets the difference. over riding is only in inheritance because it modifies the same method which is inherited )



# related general informations : 
- Primitive data types are the type which stores simple and one value like int float boolean char etc.
- Classes are blue prints for objects, blue prints meaning the original or the parent version

- so Any object in our programming language is made from a specific class

Example : 

X=10 , x is an object and its made from specific class which is int class

other example :
X=codezilla 

Print x.upper() , upper is a method that belongs to the string class 

Python interpretor would interpret the x type meaning to which class does it belong when you define it as x=........

- When you define x=1 it means its integer , then when you command x.upper() an error would show up saying int object has no attribute (method) upper it means the int class has no method called upper

-Example of method overloading: some times we find a function that work on summing two numbers like 2+4 but when you give it number and character: 2+'a' it works and give you the sum of 2 and a ascii code : this is overloading it can adapt and work in different way with different parameters
(!!!!! Its just an example doesn't mean its right, because int + character result is different from prog language to another, in some languages is an error)

Operators and specific characters are also referring to specific method of classes

Like 1+3 : + in this case is called a syntactic sugar that refer to a method called add belongs to int class
!!! this is just an example to understand the concept, bcz add method is not over ridden here, every int bool float str ... classes have their own add method, not only one add method inherited to each class


example containing class method :

We imported a class from datetime libary called date 

As you see 

We used this expression : 

Date.today().year : 

Since we imported the class without * , so we would use the class name.method with every method of the class, This is why date.today()

As we see date.today().year :

Year is clearly an attribute so its obvious that today() method would return an object of date class

So the result would be the current year - birthday year to get the age of that person

![WhatsApp Image 2025-07-11 at 13 35 46_0cc1e1dc](https://github.com/user-attachments/assets/04b293f8-7486-473d-9859-51ba55bbb34e)

![WhatsApp Image 2025-07-11 at 14 20 31_3d4ee445](https://github.com/user-attachments/assets/0899ce6a-2ea0-44c4-a17c-888fc942302e)

As you see, the first thing you should notice, that we initialized an object student2 in different way without using the class constructor, we used a class method student.initfrombirthday to initialize meaning to create this object
- but how we created an object throught this class method ?? we all know we need init function to initialize and fill the object values

this is the class method :
@classmethod

def initFromBirthYear(cls, name, birthYear):

  return cls(name, date.today().year - birthYear)

the return cls(...) it is pointing to the student class as if we wrote Student(name, age)
and we know init is automatic function in the class which is run when we class the class like when we call it by the class constructor so the init function runs with the name and age given to the class, so that's how we created an object by this class method 

so we can use class methods to create objects 


- we use decorators to define class or abstract methods : what are those decorators ?

These  decorators are special python syntax that modifies the behavior of functions or methods.

This is an example of decorators : how do they modify method behavior (what will they do) , the parameters that they take, and if they require another decorator or not

![WhatsApp Image 2025-07-12 at 13 10 17_1aee011d](https://github.com/user-attachments/assets/6a1d6e71-5d8d-404b-9ff6-940eb3b3e164)

![WhatsApp Image 2025-07-12 at 13 11 18_722be062](https://github.com/user-attachments/assets/3ff8e461-12ef-42bc-a655-9f7c6eb16b0c)



