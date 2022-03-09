from app.wsgi import *
from core.erp.models import Type

# Listar
query = Type.objects.all()
print(query)
#
#Inserción
# t = Type(name='Nicole').save()

# Edición

# t = Type.objects.get(id=1)
# t.name = 'Prestamistas'
# t.save()

# Eliminación
# t = Type.objects.all()
# t.delete()

#for i in Type.objects.filter(name__endswith='a'):
   # print(i.name)

# for a in Type.objects.all()[2:5]:
   # print(a.name)