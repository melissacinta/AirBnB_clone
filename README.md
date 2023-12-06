# AirBnB_clone

![ALX AFRICA AirBnB Clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T041631Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=89f1c392837184bf3831ded7a361ad6199cf1820558ef224c6d2f76f3343d3a7)

## Project Description

The AirBnB clone project starts from 5th december 2023 until. the end of the first year. The goal of the project is to deploy on our server a simple copy of the AirBnB website.

We won't implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and our data (retrieve, create, delete, update them)

### Final Product
By the end of the 4 months, the final product should look like this
![hbnb final look](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T033507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c9e4c1cd32f7682ee0b3a90d85d3f978a97e1b39ecda68425a27f36a27d80896)

## General concepts in review

As you navigate this code base, it is great to note the following concepts, while completing this project.

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Phase One
This is the first step towards building our first full web application which is the AirBnB clone.
Each task in this phase is linked and will help to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine


## Description of the command interpreter
| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D```  | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
