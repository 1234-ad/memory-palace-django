from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import uuid


class Palace(models.Model):
    """A memory palace - a familiar location used for memory training"""
    PALACE_TYPES = [
        ('house', 'House/Home'),
        ('school', 'School/University'),
        ('office', 'Office Building'),
        ('park', 'Park/Garden'),
        ('mall', 'Shopping Mall'),
        ('museum', 'Museum'),
        ('library', 'Library'),
        ('custom', 'Custom Location'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='palaces')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    palace_type = models.CharField(max_length=20, choices=PALACE_TYPES, default='house')
    image = models.ImageField(upload_to='palace_images/', blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.owner.username})"
    
    def get_absolute_url(self):
        return reverse('palace_detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)


class Room(models.Model):
    """A room or location within a memory palace"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    palace = models.ForeignKey(Palace, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    x_coordinate = models.FloatField(default=0.0, help_text="X position in palace layout")
    y_coordinate = models.FloatField(default=0.0, help_text="Y position in palace layout")
    
    class Meta:
        ordering = ['order', 'name']
        unique_together = ['palace', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.palace.name}"
    
    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'palace_pk': self.palace.pk, 'pk': self.pk})


class MemoryItem(models.Model):
    """An item to be remembered, placed in a specific location within a room"""
    ITEM_TYPES = [
        ('text', 'Text/Word'),
        ('number', 'Number'),
        ('name', 'Person Name'),
        ('date', 'Date'),
        ('fact', 'Fact/Information'),
        ('task', 'Task/Todo'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='memory_items')
    content = models.TextField(help_text="What you want to remember")
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, default='text')
    mnemonic_hint = models.TextField(blank=True, help_text="Memory aid or association")
    position_in_room = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='memory_items/', blank=True, null=True)
    is_mastered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['position_in_room', 'created_at']
        unique_together = ['room', 'position_in_room']
    
    def __str__(self):
        return f"{self.content[:50]}... - {self.room.name}"


class StudySession(models.Model):
    """Track study sessions for spaced repetition"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_sessions')
    palace = models.ForeignKey(Palace, on_delete=models.CASCADE, related_name='study_sessions')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    items_reviewed = models.PositiveIntegerField(default=0)
    items_mastered = models.PositiveIntegerField(default=0)
    accuracy_score = models.FloatField(default=0.0, help_text="Percentage of correct recalls")
    
    class Meta:
        ordering = ['-started_at']
    
    def __str__(self):
        return f"Study session: {self.palace.name} - {self.started_at.strftime('%Y-%m-%d %H:%M')}"
    
    @property
    def duration(self):
        if self.completed_at:
            return self.completed_at - self.started_at
        return None