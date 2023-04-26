from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from record_app.models import Employees, Files, Incoming, Outgoing
# Create your views here.
# def home_view(request):
#     return render(request, 'record_app/home.html')

class HomeView(TemplateView):
    template_name = 'record_app/home.html'

class ThankyouView(TemplateView):
    template_name = 'record_app/thankyou.html'

class EmployeeCreateView(CreateView):
    model = Employees
    fields = "__all__"
    success_url = reverse_lazy('record_app:thank_you')

class EmployeesListView(ListView):
    model = Employees
    queryset = Employees.objects.order_by("department")
    context_object_name = 'employees'

class FilesCreateView(CreateView):
    model = Files
    fields = "__all__"
    success_url = reverse_lazy('record_app:thank_you')

class FilesListView(ListView):
    model = Files
    context_object_name = 'files'

class IncomingCreateView(CreateView):
    model = Incoming
    fields = "__all__"
    success_url = reverse_lazy('record_app:thank_you')

# class IncomingListView(ListView):
#     model = Incoming
#     queryset = Incoming.objects.order_by("document_number")
#     context_object_name = 'incomings'

from django.db.models import Q

class IncomingListView(ListView):
    model = Incoming
    queryset = Incoming.objects.order_by("document_number")
    context_object_name = 'incomings'
    paginate_by = 10

    def get_queryset(self):
        search_term = self.request.GET.get('q')
        if search_term:
            queryset = Incoming.objects.filter(Q(subject__icontains=search_term) | Q(description__icontains=search_term))
        else:
            queryset = Incoming.objects.all()
        return queryset



class IncomingDetailView(DetailView):
    model = Incoming

class IncomingUpdateView(UpdateView):
    model = Incoming 
    fields = "__all__"
    success_url = reverse_lazy('record_app:thank_you')

class IncomingDeleteView(DeleteView):
    model = Incoming
    success_url = reverse_lazy('record_app:list_incoming')

class OutgoingCreateView(CreateView):
    model = Outgoing
    fields = "__all__"
    success_url = reverse_lazy('record_app:thank_you')

# class OutgoingListView(ListView):
#     model = Outgoing
#     queryset = Outgoing.objects.order_by("document_number")
#     context_object_name = 'outgoings'

class OutgoingListView(ListView):
    model = Outgoing
    queryset = Outgoing.objects.order_by("document_number")
    context_object_name = 'outgoings'
    paginate_by = 10

    def get_queryset(self):
        search_term = self.request.GET.get('q')
        if search_term:
            queryset = Outgoing.objects.filter(Q(subject__icontains=search_term) | Q(description__icontains=search_term))
        else:
            queryset = Outgoing.objects.all()
        return queryset

class OutgoingDetailView(DetailView):
    model = Outgoing

class OutgoingUpdateView(UpdateView):
    model = Outgoing
    fields = "__all__"
    success_url = reverse_lazy('record_app:thank_you')

class OutgoingDeleteView(DeleteView):
    model = Outgoing
    success_url = reverse_lazy('record_app:list_outgoing')

