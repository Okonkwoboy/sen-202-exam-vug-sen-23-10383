from django.db import models

# Create your models here.
from django.shortcuts import render


os.system('django-admin startproject chisom_staff_api')
os.chdir('chisom_staff_api')
os.system('python manage.py startapp employees')
from django.db import models

class StaffBase(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    class Meta:
        abstract = True

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='interns')
    internship_end_date = models.DateField()
    # Apply migrations
    os.system('python manage.py makemigrations employees')
    os.system('python manage.py migrate')

    # Open Django shell
    os.system('python manage.py shell')
from employees.models import Manager, Intern
import os

# Create a Manager
manager = Manager.objects.create(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    phone_number="1234567890",
    department="IT"
)

class Address(models.Model):
    """
    Reusable Address model that can be associated with any staff member
    """
    street_address = models.CharField(max_length=255)
    apartment_unit = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='United States')
    address_type = models.CharField(
        max_length=20,
        choices=[
            ('home', 'Home'),
            ('work', 'Work'),
            ('mailing', 'Mailing'),
            ('emergency', 'Emergency Contact')
        ],
        default='home'
    )
    is_primary = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'staff_address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-is_primary', 'address_type']

    def __str__(self):
        address_parts = [self.street_address]
        if self.apartment_unit:
            address_parts.append(f"Apt {self.apartment_unit}")
        address_parts.extend([self.city, self.state_province, self.postal_code])
        return ", ".join(address_parts)

