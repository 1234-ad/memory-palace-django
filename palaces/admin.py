from django.contrib import admin
from .models import Palace, Room, MemoryItem, StudySession


@admin.register(Palace)
class PalaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'palace_type', 'is_public', 'created_at']
    list_filter = ['palace_type', 'is_public', 'created_at']
    search_fields = ['name', 'owner__username', 'description']
    readonly_fields = ['id', 'created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'owner', 'description', 'palace_type', 'image', 'is_public')
        }),
        ('Metadata', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'palace', 'order', 'x_coordinate', 'y_coordinate']
    list_filter = ['palace__palace_type', 'palace__owner']
    search_fields = ['name', 'palace__name', 'description']
    readonly_fields = ['id']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'palace', 'description', 'order', 'image')
        }),
        ('Position', {
            'fields': ('x_coordinate', 'y_coordinate'),
        }),
        ('Metadata', {
            'fields': ('id',),
            'classes': ('collapse',)
        }),
    )


@admin.register(MemoryItem)
class MemoryItemAdmin(admin.ModelAdmin):
    list_display = ['content_preview', 'room', 'item_type', 'position_in_room', 'is_mastered', 'last_reviewed']
    list_filter = ['item_type', 'is_mastered', 'room__palace__palace_type', 'created_at']
    search_fields = ['content', 'mnemonic_hint', 'room__name', 'room__palace__name']
    readonly_fields = ['id', 'created_at', 'last_reviewed']
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'
    
    fieldsets = (
        (None, {
            'fields': ('room', 'content', 'item_type', 'mnemonic_hint', 'position_in_room', 'image')
        }),
        ('Progress', {
            'fields': ('is_mastered',)
        }),
        ('Metadata', {
            'fields': ('id', 'created_at', 'last_reviewed'),
            'classes': ('collapse',)
        }),
    )


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ['palace', 'user', 'started_at', 'completed_at', 'items_reviewed', 'accuracy_score']
    list_filter = ['completed_at', 'palace__palace_type', 'started_at']
    search_fields = ['palace__name', 'user__username']
    readonly_fields = ['id', 'started_at', 'duration']
    
    def duration(self, obj):
        return obj.duration
    duration.short_description = 'Session Duration'
    
    fieldsets = (
        (None, {
            'fields': ('user', 'palace', 'started_at', 'completed_at')
        }),
        ('Results', {
            'fields': ('items_reviewed', 'items_mastered', 'accuracy_score')
        }),
        ('Metadata', {
            'fields': ('id', 'duration'),
            'classes': ('collapse',)
        }),
    )