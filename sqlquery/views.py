from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format

def home(request):
    qs = Product.objects.all()
    serialize_data = serialize("json", qs)
    q = list(connection.queries)
    for qs in q:
        sqlformatted = format(str(qs['sql']), reindent=True)
        print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
    serialize_data = json.loads(serialize_data)
    return JsonResponse(serialize_data, safe=False, status=200)
