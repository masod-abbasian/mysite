from django.contrib import admin
from blog.models import POST,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# @admin.register(POST)
class POSTAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display = ('title','author','counted_view','status','login_require','published_date','created_date')
    list_filter = ('status','author')
    # ordering = ['-created_date']
    search_fields = ('title','content')
    summernote_fields = ('content',)
    

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved')
    # ordering = ['-created_date']
    search_fields = ('name','post')
    

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(POST,POSTAdmin)