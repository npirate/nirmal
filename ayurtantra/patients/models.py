from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    #note = models.
    gender_choices = (
        ('M','Male'),('F','Female'),
        )
    gender = models.CharField(max_length = 2, choices = gender_choices,)
    dob = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        get_user_model(), on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse ('patient_detail', args=[str(self.id)])

class Visit (models.Model):
    patient = models.ForeignKey (
        Patient, 
        on_delete = models.CASCADE,
        related_name ='visits',
    )
    visit_detail = models.CharField (max_length = 255)
    create_by = models.ForeignKey (
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.visit_detail[:50]

    def get_absolute_url(self):
        return reverse('patient_list')
