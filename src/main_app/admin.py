from django.contrib import admin
from .models import Project, Comment, Note

# Register your models here.

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'user_id', 'content']
    class Meta:
        model = Project

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'user_id', 'note']
    class Meta:
        model = Note

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['note','__str__', 'timestamp', 'comment',]
    class Meta:
        model = Comment    

admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Note, NoteModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
