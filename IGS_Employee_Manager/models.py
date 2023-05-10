from django.db import models

### Model class Department to define the structure of stored data
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name
        }

### Model class StaffMember to define the structure of stored data
class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'department': self.department.name
        }
