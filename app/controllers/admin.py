from app.allImports import *
from app.logic.switch import switch
from flask import flash, url_for
import flask_admin as admin
from flask_admin import form
from flask_admin.contrib.peewee import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.form.upload import FileUploadField 
from flask_admin import BaseView, expose
from flask_security import Security, roles_accepted, login_required, current_user
from flask_admin.form import rules
from flask_admin.base import AdminIndexView

class MyHomeView(AdminIndexView):
    @login_required
    @roles_accepted("Admin")
    @expose('/')
    def index(self):
        Requests = Request.select()
        Notifications = Notification.select() 
        return self.render('admin/index.html', Requests=Requests, Notifications=Notifications)

admin = admin.Admin(app, index_view=MyHomeView(), name='DAS Admin')

class UserAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')
    # Visible columns in the list view
    column_exclude_list = ['text']
    # List of columns that can be sorted. For 'user' column, use User.email as
    # a column.
    column_sortable_list = ('username', 'email', 'password', '')
    # Full text search
    column_searchable_list = ('username', 'email')
    # Column filters
    column_filters = ('username', 'email')
    
    form_create_rules = [
        # Header and four fields. Email field will go above phone field.
        rules.FieldSet(('username', 'email', 'password'), 'Personal'),
        # Separate header and few fields
        rules.Header('Confirmation'),
        rules.Field('active'),
        # String is resolved to form field, so there's no need to explicitly use `rules.Field`
        'confirmed_at','notes'
        # Show macro from Flask-Admin lib.html (it is included with 'lib' prefix)
    ]
    # Use same rule set for edit page
    form_edit_rules = form_create_rules
    
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
    
class AdminLogout(BaseView):
    @login_required
    @roles_accepted("Admin")
    @expose('/')
    def AdminLogout(self):
        return redirect('/logout')
        
class AdminUpload(BaseView):
    @login_required
    @roles_accepted("Admin")
    @expose('/')
    def AdminLogout(self):
        return self.render('admin/upload.html', cfg = cfg)
        
class StudentView(BaseView):
    @login_required
    @roles_accepted("Admin")
    @expose('/')
    def StudentView(self):
        return redirect('/index')

admin.add_view(FileDataAdmin(File, name='Files'))
admin.add_view(AdminUpload(name='Upload', endpoint='upload'))
#admin.add_view(AdminUpload(File, name='Upload'))
#admin.add_view(MyFileAdmin(path, '/static/' , name='FileUpload'))
admin.add_view(NotificationAdmin(Notification))
admin.add_view(PostAdmin(Post))
admin.add_view(UserAdmin(User))
admin.add_view(RoleAdmin(Role))
admin.add_view(UserRolesAdmin(UserRole))
admin.add_view(StudentView(name='StudentView', endpoint='studentview'))
admin.add_view(AdminLogout(name='Logout', endpoint='logout'))