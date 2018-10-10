from app.allImports import *
from app.logic.switch import switch
from flask import flash, url_for
import flask_admin as admin
from flask_admin.contrib.peewee import ModelView
from flask_admin import BaseView, expose
from flask_security import Security, roles_accepted, login_required, current_user

admin = admin.Admin(app)

class UserAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    # Visible columns in the list view
    column_exclude_list = ['text']
    
class RoleAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    can_delete = False
    # Visible columns in the list view
    column_exclude_list = ['text']
    
class UserRolesAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    # Visible columns in the list view
    column_exclude_list = ['text']
<<<<<<< HEAD
=======
    

class PostAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    # Visible columns in the list view
    column_exclude_list = ['text']
    # List of columns that can be sorted. For 'user' column, use User.email as
    # a column.
    column_sortable_list = ('title', ('user', User.email), '')
    # Full text search
    column_searchable_list = ('title', User.username)
    # Column filters
    column_filters = ('title',
                      'date',
                      User.username)
                    
class NotificationAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    # Visible columns in the list view
    column_exclude_list = ['text']
    # List of columns that can be sorted. For 'user' column, use User.email as
    # a column.
    column_sortable_list = ('title', ('user', User.email), '')
    # Full text search
    column_searchable_list = ('title', User.username)
    # Column filters
    column_filters = ('title',
                      'date',
                      User.username)
                      
class RequestAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    # Visible columns in the list view
    column_exclude_list = ['text']
    # List of columns that can be sorted. For 'user' column, use User.email as
    # a column.
    column_sortable_list = ('title''title', 'author', 'edition', '')
    # Full text search
    column_searchable_list = ('title', User.username)
    # Column filters
    column_filters = ('title',
                      'created_at',
                      User.username)
    
class FileDataAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    can_create = False
    # Visible columns in the list view
    column_exclude_list = ['text']
    # List of columns that can be sorted. For 'user' column, use User.email as
    # a column.
    column_sortable_list = ('title', 'author', 'edition',
                            'size', 'filename', 'file_type',
                            'created_at','last_modified',
                            'asigned',
                            'file_path', 'hidden')

    # Full text search
    column_searchable_list = ('title', User.username)
    # Column filters
    column_filters = ('title', 'author', 'edition',
                        'size', 'filename', 'file_type',
                        User.username,)
                        
class MyFileAdmin(FileAdmin):
    def is_accessible(self):
        return current_user.has_role('Admin')
    allowed_extensions = ('pdf', 'docx', 'doc', 'xml')


class AdminUpload(ModelView):
    form_create_rules = [
        # Header and four fields. Email field will go above phone field.
        rules.FieldSet(('title','filename', 'author', 'edition', 'file_type' ,
        'created_at' , 'last_modified_by' , 'last_modified' , 
        'file_path' , 'size'), 'File Data'),
        # Separate header and few fields
        rules.Header('Admin'),
        rules.Field('hidden')
    ]
    form_overrides = {
        'filename': form.FileUploadField
    }

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'filename': {
            'label': 'File',
            'base_path': path,
            'allow_overwrite': True}}
    # Use same rule set for edit page
>>>>>>> parent of 9e7bcc7... Mering with master
    
class AdminLogout(BaseView):
    @login_required
    @roles_accepted("Admin")
    @expose('/')
    def AdminLogout(self):
        return redirect('/logout')

<<<<<<< HEAD
=======
admin.add_view(FileDataAdmin(File, name='Files'))
admin.add_view(AdminUpload(name='Upload', endpoint='upload'))
#admin.add_view(AdminUpload(File, name='Upload'))
#admin.add_view(MyFileAdmin(path, '/static/' , name='FileUpload'))
admin.add_view(NotificationAdmin(Notification))
admin.add_view(RequestAdmin(Request))
admin.add_view(PostAdmin(Post))
>>>>>>> parent of 9e7bcc7... Mering with master
admin.add_view(UserAdmin(User))
admin.add_view(RoleAdmin(Role))
admin.add_view(UserRolesAdmin(UserRole))
admin.add_view(AdminLogout(name='Logout', endpoint='logout'))