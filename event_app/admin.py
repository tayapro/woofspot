from django.contrib import admin
from django.shortcuts import get_object_or_404
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from cloudinary.uploader import destroy
from .models import WoofspotEvent


@admin.register(WoofspotEvent)
class WoofspotEventAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing WoofspotEvent models.

    This class customizes the Django admin interface to allow for:
    - Displaying key event details like title, slug, and image.
    - Enabling search and filtering by event attributes.
    - Handling image previews and providing a way to delete images.
    """

    list_display = ('title', 'slug', 'created_on', 'image_preview')
    search_fields = ['title', 'description']
    list_filter = ('location', 'date', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        """
        Generates an image preview with a link to delete the image.

        Displays an image preview for the event if it exists.
        Provides a link to delete the image if one is present.

        Args:
            obj: The WoofspotEvent instance for which the preview is generated.

        Returns:
            A formatted HTML string with an image and a delete link,
            or 'No Image' if no image exists.
        """

        if obj.image:
            delete_url = reverse('admin:event_app_woofspotevent_delete_image',
                                 args=[obj.id])

            return format_html(
                '<img src="{}" width="150" height="auto" />'
                '<br><a href="{}">Delete Image</a>',
                obj.image.url,
                delete_url

            )
        return "No Image"

    image_preview.short_description = "Image Preview"

    def delete_image(self, request, event_id, *args, **kwargs):
        """
        Deletes the image associated with a WoofspotEvent.

        If the event has an image, it is removed, and a success message is
        shown. If no image is found, a message stating "No image" is displayed.

        Args:
            request: The HTTP request object.
            event_id: The ID of the event for which the image is being deleted.

        Returns:
            A redirect to the event list page in the admin interface.
        """

        if not self.has_change_permission(request):
            raise PermissionDenied

        try:
            event = get_object_or_404(WoofspotEvent, id=event_id)

            if event.image:
                event.remove_image()
                self.message_user(request, "Image successfully removed")
            else:
                self.message_user(request, "No image.")
            url = reverse('admin:event_app_woofspotevent_changelist')
            return HttpResponseRedirect(url)

        except Exception as ex:
            self.message_user(request, f"Could not delete: {ex}")
            url = reverse('admin:event_app_woofspotevent_changelist')
            return HttpResponseRedirect(url)

    def get_urls(self):
        """
        Override the default `get_urls` method to add a custom URL for
        deleting event images.

        This method adds a custom URL pattern for deleting the event image
        from the admin interface.

        Returns:
            List of URLs, including the default ones and the custom image
            deletion URL.
        """

        urls = super().get_urls()
        new_urls = [
             path('<int:event_id>/delete-image/',
                  self.admin_site.admin_view(self.delete_image),
                  name='event_app_woofspotevent_delete_image'),
        ]
        return new_urls + urls
