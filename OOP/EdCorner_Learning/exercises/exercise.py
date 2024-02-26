class Person:
    # constructor
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname;
        self.lastname = lastname;
        self.age = age;

class Department:
    # constructor
    def __init__(self, deptname: str, short_dept_name: str) -> None:
        self.deptname = deptname
        self.short_dept_name = short_dept_name

class Worker(Person, Department):
    # constructor
    def __init__(self, firstname: str, lastname: str, age: int, deptname: str, short_dept_name: str) -> None:
        super().__init__(self, firstname, lastname, age)
        Department.__init__(self, deptname, short_dept_name)