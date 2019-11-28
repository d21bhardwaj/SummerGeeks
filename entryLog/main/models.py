from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.utils.timezone import now


department_choices = [
    ('Finance','Finance'),
    ('HR','HR'),
    ('Legal','Legal'),
    ('Product Management','Product Management'),
    ('Software','Software'),

]
title_choices = [
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Dr.','Dr.'),
    ('Judge','Judge'),
    ('Professor','Professor'),
]

class Employee(models.Model):
    title = models.CharField(max_length=10,blank=True, choices=title_choices,default='')
    name = models.CharField(max_length=181)
    designation = models.CharField(max_length=40, null=True, blank=True)
    phone_no = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    email = models.EmailField(max_length=70, unique=True)
    department = models.CharField(max_length=40, null=True, blank=True)
    room_no = models.CharField(max_length=40, null=True, blank=True)
    in_office = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.name, self.email)


class Entry(models.Model):
    visitor_title = models.CharField(max_length=10,blank=True, choices=title_choices,default='')
    visitor_name = models.CharField(max_length=181, blank=True)
    visitor_phone_no = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    visitor_email = models.EmailField(max_length=70)
    in_time = models.DateTimeField(default=now)
    out_time = models.DateTimeField(null=True, blank=True)
    left_office = models.BooleanField(default=False)
    verification = models.IntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1111)], blank=True, null=True, default=None )

    # Information of the host can be accessed through Employee table 
    host_name = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null = False)
    def __str__(self):
        return str(self.id)
