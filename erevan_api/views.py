from django.http import JsonResponse
from django.shortcuts import render

from .models import *


def get_team_members(request):
    resp = []
    members = TeamMember.objects.all()
    for member in members:
        member_json = {
            'id': member.id,
            'name': member.name,
            'photo_path': member.photo_path,
            'role': member.role,
            'description': member.description,
            'tags': member.tags.split('\r\n'),
            'social_networks': []
        }
        for social in member.social_networks.split('\r\n'):
            social = {
                'path': social.split('$')[0],
                'network_name': social.split('$')[1],
            }
            member_json['social_networks'].append(social)
        resp.append(member_json)
    return JsonResponse(resp, safe=False)


def get_activities(request):
    resp = []
    members = Activity.objects.all()
    for member in members:
        json = {
            'img': member.img,
            'header': member.header,
            'text': member.text,
        }
        resp.append(json)
    return JsonResponse(resp, safe=False)


def get_header_description(request):
    members = HeaderDescription.objects.filter().last()
    resp = {
        'header': members.header,
        'subheader': members.subheader,
        'text': members.text.split('$$')
    }
    return JsonResponse(resp, safe=False)


def get_cases(request):
    resp = []
    members = Case.objects.all()
    for member in members:
        json = {
            'header': member.header,
            'text': member.text.split('$$'),
            'tags': member.tags.split('\r\n'),
        }
        resp.append(json)
    return JsonResponse(resp, safe=False)


def get_header_reasons(request):
    resp = []
    members = HeaderReasons.objects.all()
    for member in members:
        resp.append(member.text)
    return JsonResponse(resp, safe=False)