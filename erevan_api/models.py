"""Тестовое API для сайта разработчиков"""
from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    photo_path = models.TextField()
    role = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.TextField()
    social_networks = models.TextField()

class HeaderDescription(models.Model):
    header = models.TextField()
    subheader = models.TextField()
    text = models.TextField()

class HeaderReasons(models.Model):
    text = models.TextField()

class Activity(models.Model):
    img = models.TextField()
    header = models.TextField()
    text = models.TextField()

class Case(models.Model):
    header = models.TextField()
    tags = models.TextField()
    text = models.TextField()