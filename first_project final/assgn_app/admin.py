from django.contrib import admin

# Register your models here.
from .models import Student,Professor,AssignmentQ,Subject,AssignmentA,StudSub
#from .forms import UploadFileForm

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(AssignmentA)
admin.site.register(Subject)
admin.site.register(AssignmentQ)
admin.site.register(StudSub)
#admin.site.register(UploadFileForm)
