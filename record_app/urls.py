from django.urls import path
from .views import HomeView, ThankyouView, EmployeeCreateView, EmployeesListView, FilesCreateView, FilesListView, IncomingCreateView, IncomingListView, IncomingDetailView, IncomingUpdateView, IncomingDeleteView, OutgoingCreateView, OutgoingListView, OutgoingDetailView, OutgoingUpdateView, OutgoingDeleteView

app_name = 'record_app'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('thankyou/',ThankyouView.as_view(), name='thank_you'),
    path('create_employee/', EmployeeCreateView.as_view(), name='create_employee'),
    path('list_employees/', EmployeesListView.as_view(), name='list_employees'),
    path('create_file/', FilesCreateView.as_view(), name='create_files'),
    path('list_files/', FilesListView.as_view(), name="list_files"),
    path('create_incoming/', IncomingCreateView.as_view(), name="create_incoming"),
    path('list_incoming/', IncomingListView.as_view(), name="list_incoming"),
    path('detail_incoming/<int:pk>', IncomingDetailView.as_view(), name="detail_incoming"),
    path('update_incoming/<int:pk>', IncomingUpdateView.as_view(), name="update_incoming"),
    path('delete_incoming/<int:pk>', IncomingDeleteView.as_view(), name="delete_incoming"),
    path('create_outgoing/', OutgoingCreateView.as_view(), name="create_outgoing"),
    path('list_outgoing/', OutgoingListView.as_view(), name="list_outgoing"),
    path('detail_outgoing/<int:pk>', OutgoingDetailView.as_view(), name="detail_outgoing"),
    path('update_outgoing/<int:pk>', OutgoingUpdateView.as_view(), name="update_outgoing"),
    path('delete_outgoing/<int:pk>', OutgoingDeleteView.as_view(), name="delete_outgoing"),
]