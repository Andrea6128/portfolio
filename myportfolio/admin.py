from django.contrib import admin
from .models import Personal
from .models import Contact
from .models import Skill
from .models import History
from .models import Course
from .models import Portfolio


# Register your models here.
admin.site.register(Personal)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(History)
admin.site.register(Course)
admin.site.register(Portfolio)