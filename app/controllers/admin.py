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
    
class AdminLogout(BaseView):
    @login_required
    @roles_accepted("Admin")
    @expose('/')
    def AdminLogout(self):
        return redirect('/logout')

admin.add_view(UserAdmin(User))
admin.add_view(RoleAdmin(Role))
admin.add_view(UserRolesAdmin(UserRole))
admin.add_view(AdminLogout(name='Logout', endpoint='logout'))