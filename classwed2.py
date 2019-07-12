class nagarro:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

p1 = nagarro("deepanshu", 3151405)
p2 = nagarro("kshitij", 1234567)
p3 = nagarro("UG", 3151433)

print(p1.name, " has emp id : ", p1.emp_id)
print(p2.name, " has emp id : ", p2.emp_id)
print(p3.name, " has emp id : ", p3.emp_id)