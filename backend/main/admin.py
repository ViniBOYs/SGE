from django.contrib import admin
from .models import *

# Register your models here.

class AdminCustomUser(admin.ModelAdmin):
    list_display = ('id','email','registrationNumber','is_active')
    list_display_links = ('id','email','registrationNumber','is_active',)
    search_fields = ('email','registrationNumber')
    list_per_page = 10
admin.site.register(CustomUser,AdminCustomUser)

class AdminEnvironments(admin.ModelAdmin):
    list_display = ('id','name','block')
    list_display_links = ('id','name','block',)
    search_fields = ('name','block')
    list_per_page = 10
admin.site.register(Environments,AdminEnvironments)

class AdminTasks(admin.ModelAdmin):
    list_display = ('id','environmentFK','title','reporterFK')
    list_display_links = ('id','environmentFK','title','reporterFK')
    search_fields = ('name','reporterFK')
    list_per_page = 10
admin.site.register(Tasks,AdminTasks)

# class AdminTasksAssignees(admin.ModelAdmin):
#     list_display = ('id','taskFK','assigneeFK')
#     list_display_links = ('id','taskFK','assigneeFK',)
#     search_fields = ('taskFK')
#     list_per_page = 10
# admin.site.register(TasksAssignees.AdminTasksAssignees)

class AdminTasksAssignees(admin.ModelAdmin):
    list_display = ('id','taskFK','assigneeFK')
    list_display_links = ('id','taskFK','assigneeFK',)
    search_fields = ('taskFK','assigneeFK')
    list_per_page = 10
admin.site.register(TasksAssignees,AdminTasksAssignees)


class AdminEquipments(admin.ModelAdmin):
    list_display = ('id','name','assigneeFK')
    list_display_links = ('id','name','assigneeFK',)
    search_fields = ('name','assigneeFK')
    list_per_page = 10
admin.site.register(Equipments,AdminEquipments)

class AdminTasksStatus(admin.ModelAdmin):
    list_display = ('id','taskFK','status','creationDate')
    list_display_links = ('id','taskFK','status','creationDate')
    search_fields = ('taskFK','status','creationDate')
    list_per_page = 10
admin.site.register(TasksStatus,AdminTasksStatus)

class AdminFilesTasksStatus(admin.ModelAdmin):
    list_display = ('id','taskStatusFK','equipamentFK')
    list_display_links = ('id','taskStatusFK','equipamentFK',)
    search_fields = ('equipamentFK',)
    list_per_page = 10
admin.site.register(FilesTasksStatus,AdminFilesTasksStatus)

class AdminEnviromentsAssignees(admin.ModelAdmin):
    list_display = ('id','environmentFK','assigneeFK')
    list_display_links = ('id','environmentFK','assigneeFK',)
    search_fields = ('environmentFK',)
    list_per_page = 10
admin.site.register(EnviromentsAssignees,AdminEnviromentsAssignees)

class AdminThemes(admin.ModelAdmin):
    list_display = ('id','name','timeLoad')
    list_display_links = ('id','name','timeLoad',)
    search_fields = ('name',)
    list_per_page = 10
admin.site.register(Themes,AdminThemes)

class AdminCourses(admin.ModelAdmin):
    list_display = ('id','name','category','duration','area')
    list_display_links = ('id','name','duration','area',)
    search_fields = ('name',)
    list_per_page = 10
admin.site.register(Courses,AdminCourses)

class AdminCoursesThemes(admin.ModelAdmin):
    list_display = ('id','curseFK','themeFK')
    list_display_links = ('id','curseFK','themeFK',)
    search_fields = ('curseFK','themeFK')
    list_per_page = 10
admin.site.register(CoursesThemes,AdminCoursesThemes)

class AdminClasses(admin.ModelAdmin):
    list_display = ('id','name','startDate','endDate')
    list_display_links = ('id','name','startDate',)
    search_fields = ('curseFK','themeFK')
    list_per_page = 10
admin.site.register(Classes,AdminClasses)

class AdminClassesDivision(admin.ModelAdmin):
    list_display = ('id','name','classFK')
    list_display_links = ('id','name','classFK',)
    search_fields = ('id','classFK',)
    list_per_page = 10
admin.site.register(ClassesDivision,AdminClassesDivision)

class AdminTeachersAlocation(admin.ModelAdmin):
    list_display = ('id','classFK','ThemeFK','reporterFK')
    list_display_links = ('id','classFK','reporterFK',)
    search_fields = ('id','classFK','reporterFK')
    list_per_page = 10
admin.site.register(TeachersAlocation,AdminTeachersAlocation)

class AdminTeacherAlocationDetail(admin.ModelAdmin):
    list_display = ('id','creationDate','updateDate','alocationStatus','CustomUserFK','classDivisionFK')
    list_display_links = ('id','creationDate','alocationStatus','CustomUserFK','classDivisionFK')
    search_fields = ('id','creationDate','CustomUserFK')
    list_per_page = 10
admin.site.register(TeacherAlocationDetail,AdminTeacherAlocationDetail)

class AdminTeacherAlocationDetailEnv(admin.ModelAdmin):
    list_display = ('id','weekDay','teacherAlocationDetailFK','startDate','enviromentFK')
    list_display_links = ('id','weekDay','teacherAlocationDetailFK',)
    search_fields = ('id','weekDay','teacherAlocationDetailFK')
    list_per_page = 10
admin.site.register(TeacherAlocationDetailEnv,AdminTeacherAlocationDetailEnv)

class AdminDeadline(admin.ModelAdmin):
    list_display = ('id','targetDate','category')
    list_display_links = ('id','targetDate','category',)
    search_fields = ('id','classFK')
    list_per_page = 10
admin.site.register(Deadline,AdminDeadline)

class AdminSignatures(admin.ModelAdmin):
    list_display = ('id','ownerFK','Signature')
    list_display_links = ('id','ownerFK','Signature',)
    search_fields = ('id','ownerFK')
    list_per_page = 10
admin.site.register(Signatures,AdminSignatures)

class AdminPlan(admin.ModelAdmin):
    list_display = ('id','CustomUserFK','CoursesThemesFK','status','approverFK')
    list_display_links = ('id','CustomUserFK','status','approverFK',)
    search_fields = ('id','CustomUserFK')
    list_per_page = 10
admin.site.register(Plan,AdminPlan)

class AdminPlanStatus(admin.ModelAdmin):
    list_display = ('id','planFK','createdDate','status')
    list_display_links = ('id','planFK','createdDate','status',)
    search_fields = ('id','status')
    list_per_page = 10
admin.site.register(PlanStatus,AdminPlanStatus)












