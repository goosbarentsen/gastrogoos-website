from django.contrib import admin
from projects.models import Project,ProjectImage

#class ProjectAdmin(admin.ModelAdmin):
#    pass
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

#admin.site.register(ProjectImage, PropertyAdmin)    
admin.site.register(Project, ProjectAdmin)

