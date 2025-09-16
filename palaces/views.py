from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils import timezone
from .models import Palace, Room, MemoryItem, StudySession
from .forms import PalaceForm, RoomForm, MemoryItemForm


class PalaceListView(LoginRequiredMixin, ListView):
    model = Palace
    template_name = 'palaces/palace_list.html'
    context_object_name = 'palaces'
    paginate_by = 12
    
    def get_queryset(self):
        return Palace.objects.filter(owner=self.request.user)


class PalaceDetailView(LoginRequiredMixin, DetailView):
    model = Palace
    template_name = 'palaces/palace_detail.html'
    context_object_name = 'palace'
    
    def get_queryset(self):
        return Palace.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.object.rooms.all()
        context['total_items'] = sum(room.memory_items.count() for room in context['rooms'])
        context['mastered_items'] = sum(room.memory_items.filter(is_mastered=True).count() for room in context['rooms'])
        return context


class PalaceCreateView(LoginRequiredMixin, CreateView):
    model = Palace
    form_class = PalaceForm
    template_name = 'palaces/palace_form.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Memory palace created successfully!')
        return super().form_valid(form)


class PalaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Palace
    form_class = PalaceForm
    template_name = 'palaces/palace_form.html'
    
    def get_queryset(self):
        return Palace.objects.filter(owner=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Memory palace updated successfully!')
        return super().form_valid(form)


class PalaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Palace
    template_name = 'palaces/palace_confirm_delete.html'
    success_url = reverse_lazy('palace_list')
    
    def get_queryset(self):
        return Palace.objects.filter(owner=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Memory palace deleted successfully!')
        return super().delete(request, *args, **kwargs)


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'palaces/room_detail.html'
    context_object_name = 'room'
    
    def get_object(self):
        palace = get_object_or_404(Palace, pk=self.kwargs['palace_pk'], owner=self.request.user)
        return get_object_or_404(Room, pk=self.kwargs['pk'], palace=palace)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['palace'] = self.object.palace
        context['memory_items'] = self.object.memory_items.all()
        return context


@login_required
def room_create(request, palace_pk):
    palace = get_object_or_404(Palace, pk=palace_pk, owner=request.user)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.palace = palace
            room.save()
            messages.success(request, 'Room added successfully!')
            return redirect('palace_detail', pk=palace.pk)
    else:
        form = RoomForm()
    
    return render(request, 'palaces/room_form.html', {
        'form': form,
        'palace': palace,
        'title': 'Add Room'
    })


@login_required
def memory_item_create(request, palace_pk, room_pk):
    palace = get_object_or_404(Palace, pk=palace_pk, owner=request.user)
    room = get_object_or_404(Room, pk=room_pk, palace=palace)
    
    if request.method == 'POST':
        form = MemoryItemForm(request.POST, request.FILES)
        if form.is_valid():
            memory_item = form.save(commit=False)
            memory_item.room = room
            memory_item.save()
            messages.success(request, 'Memory item added successfully!')
            return redirect('room_detail', palace_pk=palace.pk, pk=room.pk)
    else:
        form = MemoryItemForm()
    
    return render(request, 'palaces/memory_item_form.html', {
        'form': form,
        'palace': palace,
        'room': room,
        'title': 'Add Memory Item'
    })


@login_required
def start_study_session(request, palace_pk):
    palace = get_object_or_404(Palace, pk=palace_pk, owner=request.user)
    
    # Create new study session
    session = StudySession.objects.create(
        user=request.user,
        palace=palace
    )
    
    return redirect('study_session', session_pk=session.pk)


@login_required
def study_session(request, session_pk):
    session = get_object_or_404(StudySession, pk=session_pk, user=request.user)
    
    if request.method == 'POST':
        # Handle study session completion
        session.completed_at = timezone.now()
        session.items_reviewed = int(request.POST.get('items_reviewed', 0))
        session.items_mastered = int(request.POST.get('items_mastered', 0))
        if session.items_reviewed > 0:
            session.accuracy_score = (session.items_mastered / session.items_reviewed) * 100
        session.save()
        
        messages.success(request, f'Study session completed! Accuracy: {session.accuracy_score:.1f}%')
        return redirect('palace_detail', pk=session.palace.pk)
    
    # Get all memory items for this palace
    rooms = session.palace.rooms.all()
    memory_items = []
    for room in rooms:
        memory_items.extend(room.memory_items.all())
    
    return render(request, 'palaces/study_session.html', {
        'session': session,
        'palace': session.palace,
        'rooms': rooms,
        'memory_items': memory_items,
    })


@login_required
def toggle_mastery(request, item_pk):
    """AJAX view to toggle memory item mastery status"""
    if request.method == 'POST':
        memory_item = get_object_or_404(MemoryItem, pk=item_pk, room__palace__owner=request.user)
        memory_item.is_mastered = not memory_item.is_mastered
        memory_item.last_reviewed = timezone.now()
        memory_item.save()
        
        return JsonResponse({
            'success': True,
            'is_mastered': memory_item.is_mastered
        })
    
    return JsonResponse({'success': False})