from django.contrib import admin
# Register your models here.
from .models import Location, PickupRequest
from twilio.rest import Client


@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ('location', 'status', 'description',
                    'type', 'phone_number',)
    actions = ('accept_request', 'reject_request',)
    search_fields = ('location', 'description', 'phone_number')

    def save_model(self, request, obj, form, change):
        obj.phone_number = form.cleaned_data['phone_number']
        if(obj.status == 'A'):
            client = Client('AC916570d285355980fa8406cba9c38f42',
                            '69122bb98b474f4d02971e829f72ed42')
            message = client.messages.create(
                to=(obj.phone_number),
                from_="+12173878678",
                body="Your request has been accepted. Thank you for using our service."
            )
            self.message_user(
                request, "SMS sent successfully to %s" % obj.phone_number)
        obj.save()

    def accept_request(self, request, queryset):
        queryset.update(status='A')
        for obj in queryset:
            client = Client('AC916570d285355980fa8406cba9c38f42',
                            '69122bb98b474f4d02971e829f72ed42')
            message = client.messages.create(
                to=(obj.phone_number),
                from_="+12173878678",
                body="Your request has been accepted. Thank you for using our service."
            )
            self.message_user(
                request, "SMS sent successfully to %s" % obj.phone_number)

    def reject_request(self, request, queryset):
        queryset.update(status='R')
        for obj in queryset:
            client = Client('AC916570d285355980fa8406cba9c38f42',
                            '69122bb98b474f4d02971e829f72ed42')
            message = client.messages.create(
                to=(obj.phone_number),
                from_="+12173878678",
                body="Your request has been rejected."
            )
            self.message_user(
                request, "SMS sent successfully to %s" % obj.phone_number)

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Location)
