from app.wsgi import *
from core.erp.models import *

# listar

for i in Category.objects.filter():
    print(i)

