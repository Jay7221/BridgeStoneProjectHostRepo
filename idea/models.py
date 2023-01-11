from django.db import models
from account.models import Profile
from django.contrib.auth.models import User
from program.models import BusinessUnit, Program
from django.utils import timezone
from django.core.mail import send_mail
from IdeaManagementPlatform.settings import EMAIL_HOST_USER

# Create your models here.


class Idea(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Active'),
        (2, 'Handoff'),
        (3, 'Completed'),
        (4, 'Paused'),
        (5, 'Stopped'),
        (6, 'Put On Hold'),
        (7, 'Rejected'),
    )
    fields = ['Pending', 'Active', 'Handoff', 'Completed',
              'Paused', 'Stopped', 'Put On Hold', 'Rejected']

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.png',
                              upload_to='static/images/')
    business_unit = models.ForeignKey(
        BusinessUnit, null=True, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    ideator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    projected_revenue = models.BigIntegerField(null=True, default=0)
    actual_net_revenue = models.BigIntegerField(null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def accept(self):
        self.status = 1

    def reject(self):
        self.status = 6

    def putOnHold(self):
        self.status = 7

    def getStatus(self):
        return self.STATUS_CHOICES[self.status][1]

    def send_apply_email(self):
        program = self.program
        to_mail_list = [program.coordinator.email,
                        program.business_unit.jury.email, self.ideator.email]
        subject = f"Idea applied for project {program.name}"
        message = self.title + '\n' + self.summary
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            to_mail_list,
            fail_silently=False
        )

    def change_of_status_mail(self):
        program = self.program
        to_mail_list = [program.coordinator.email,
                        program.business_unit.jury.email]
        subject = f"Idea Status Changed to {self.getStatus()} for Idea {self.title}"
        message = self.title + '\n' + self.summary
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            to_mail_list,
            fail_silently=True
        )

    class Meta:
        ordering = ['-updated', '-created']
