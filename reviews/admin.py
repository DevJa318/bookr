from django.contrib import admin

from reviews.models import Publisher, Contributor, Book, BookContributor, Review
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')
    date_hierarchy = 'publication_date'
    list_filter = ('publisher', )
    search_fields = ('title', 'isbn', 'publisher__name',)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names', 'first_names')

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited', )


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)