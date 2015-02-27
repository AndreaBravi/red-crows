from django.contrib import admin
from framework.models import Choice, Poll, Musician, Reviewer, Review, MusicianProduct

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')

admin.site.register(Poll, PollAdmin)

class MusicianAdmin(admin.ModelAdmin):
    pass

class ReviewerAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

class MusicianProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Musician, MusicianAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(MusicianProduct, MusicianProductAdmin)


