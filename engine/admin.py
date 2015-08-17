from django.contrib import admin
from engine.models import Project, Task
# import xadmin
from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin

# admin.site.register(Actor)
# admin.site.register(Role)
admin.site.register(Task)


class ProjectAdmin(MPTTModelAdmin, SortableModelAdmin):
	mptt_level_indent = 20
	list_display = ('p_name', 'p_id', 'active_status')
	list_editable = ('active_status',)

	# Specify name of sortable property
	sortable = 'order'

admin.site.register(Project, ProjectAdmin)



