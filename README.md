# Course Management Database System
Using Python, Flask, SQLAlchemy, and PostgreSQL

This project includes:
* Entity Relationship Diagram
* Course Management HTTP Requests via Insomnia
* Creation of the entire database in SQL
* Courses Blueprint in Python
* Departments Blueprint in Python
* Instructors Blueprint in Python
* Models.py that ties in all the blueprints for courses, departments, instructors, and students
* Pg_dump.Sql
* Students Blueprint in Python

## API Reference Table
Students API
| Name | HTTP Method | Parameter | 
|------|-------------|-----------|
| Update | PUT | {{base_url}}/students/:id |
| Delete | DELETE | {{base_url}}/students/:id |
| Create | POST | {{base_url}}/students |
| Show | GET | {{base_url}}/students/:id |
| Index | GET | {{base_url}}/students |

Instructor API
| Name | HTTP Method | Parameter | 
|------|-------------|-----------|
| Update | PUT | {{base_url}}/instructors/:id |
| Delete | DELETE | {{base_url}}/instructors/:id |
| Create | POST | {{base_url}}/instructors |
| Show | GET | {{base_url}}/instructors/:id |
| Index | GET | {{base_url}}/instructors |

Departments API
| Name | HTTP Method | Parameter |
| --- | --- | --- |
| Delete | DELETE | {{base_url}}/departments/:id | 
| Create | POST | {{base_url}}/departments |
| Show | GET | {{base_url}}/departments/:id |
| Index | GET | {{base_url}}/departments |

Courses API
| Name | HTTP Method | Parameter |
| --- | --- | --- |
| Delete | DELETE | {{base_url}}/courses/:id |
| Add | POST | {{base_url}}/courses |
| Show | GET | {{base_url}}/courses/:id |
| Index | GET | {{base_url}}/courses |

## Project Reflection
The project evolved as my understanding of SQL, ORM, and flask continued. While I still have some areas that I can vastly improve, the only way to go from here is up. For the purposes of this project I chose to implement an ORM using Flask so as to grasp a better understanding. An improvement I could see is implementing a feature where a student can look up the books they need based on the classes they are registered for. 
