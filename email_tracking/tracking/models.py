from django.db import models
from .choices import MATCH_STATE_CHOICES, CANDIDATE_INTEREST_CHOICES, JOB_STATE_CHOICES


class Match(models.Model):
    state = models.CharField(max_length=20, choices=MATCH_STATE_CHOICES, default='in_progress')
    candidate_interest = models.CharField(max_length=20, choices=CANDIDATE_INTEREST_CHOICES, default='interested')
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.state + " " + self.candidate_interest


class Job(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="title")
    state = models.CharField(max_length=20, choices=JOB_STATE_CHOICES, default='open')

    def __str__(self):
        return self.title + " " + self.state


class Candidate(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="name")
    email = models.EmailField(max_length=100, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.email


class Event(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True, verbose_name="event_type")
    message_id = models.CharField(max_length=250, null=True, blank=True, verbose_name="event_msg_id")
    match_id = models.CharField(max_length=250, null=True, blank=True, verbose_name="event_match_id")
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Msg Type " + str(self.type)


class Email(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="event_source")
    is_created = models.BooleanField(default=False)
    is_bounced = models.BooleanField(default=False)
    is_responded = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Msg Type " + str(self.is_created)
