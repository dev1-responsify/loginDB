# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from loginDB.models import LoginDB
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def viewer(request):
    # Creating an Entry

    loginDB5 = LoginDB(
        user_name="Burt", email="burt@gmail.com", password="york")
    # Saving an Entry
    loginDB5.save()

    # Reading all entries
    # puts all LoginDB objects in an array and loops through while adding a page break to each one.
    entries = LoginDB.objects.all()
    res = 'Showing all entries in the database: <br>'

    for each in entries:
        res += each.user_name + "<br>"

    return HttpResponse(res)
