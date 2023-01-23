from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    title_header = 'Aplikacja administracyjna Bookr'
    site_header = 'Aplikacja Administracyjna Bookr'
    index_title = 'Administracja witryną Bookr'