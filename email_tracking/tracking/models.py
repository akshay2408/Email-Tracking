from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
import datetime
from .choices import MATCH_STATE_CHOICES, CANDIDATE_INTEREST_CHOICES, JOB_STATE_CHOICES


class Job(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="title")
    state = models.CharField(max_length=20, choices=JOB_STATE_CHOICES, default='open')

    def __str__(self):
        return self.title + " " + self.state


class Candidate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="name")
    email = models.EmailField(max_length=100, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.email


class Match(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name="candidate_source")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, related_name="job_source")
    state = models.CharField(max_length=20, choices=MATCH_STATE_CHOICES, default='in_progress')
    candidate_interest = models.CharField(max_length=20, choices=CANDIDATE_INTEREST_CHOICES, default='interested')
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.state + " " + self.candidate_interest


class Event(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True, verbose_name="event_type")
    metadata_information = JSONField()
    create_at = models.DateField(default=datetime.date.today())

    def __str__(self):
        return "Msg Type " + str(self.type)

    def clean(self):
        if self.create_at > datetime.date.today():  # 🖘 raise error if greater than
            raise ValidationError("The date cannot be in the past!")
        return self.create_at


class Email(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="event_source")
    is_created = models.BooleanField(default=False)
    is_bounced = models.BooleanField(default=False)
    is_responded = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Msg Type " + str(self.is_created)
