from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Pages 
    path('', views.leave_dashboard_page, name="leave_dashboard_page"),
    path('types/', views.leave_types_page, name="leave_types_page"),
    path('holidays/', views.holidays_page, name="holidays_page"),
    path('path/', views.approval_path_page, name="path_page"),
    path('apply/', views.apply_leave_page, name="apply_leave_page"),
    
    # Process
    path('add_new_type/', views.add_new_type, name="add_new_type"),
    path('edit_type/<int:id>/', views.edit_leave_type_page, name="edit_leave_type_page"),
    path('add_new_holiday/', views.add_new_holiday, name="add_new_holiday"),
    path('add_new_path/', views.add_new_path, name="add_new_path"),
    path('apply_leave/', views.apply_leave, name="apply_leave"),
    path('approve_leave/', views.approve_leave, name="approve_leave"),
    
    path('annual_calendar/', views.Leave_planner_summary, name="annual_calendar"),
    path('leave_planner/', views.leave_planer, name="leave_planner"),
    path('add_new_absence/', views.add_new_absence, name="add_new_absence"),
    path('Leave_planner_summary/', views.Leave_planner_summary, name="Leave_planner_summary"),
    path('leave_calendar/', views.leave_calendar, name="Leave_calendar"),

]