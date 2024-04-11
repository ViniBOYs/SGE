from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import *

#criando uma classe de usuário customizada para substituir a padrão com
#atributos desejados:
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email" #substituir o login username por e-mail
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email    


BLOCKS = [
    ('A','Bloco A'),
    ('B','Bloco B'),
    ('C','Bloco C'),
]

class Environments(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30, choices=BLOCKS)

    def __str__(self):
        return self.name

TASKS_TYPE = [
    ('MA','Manutenção'),
    ('ME','Melhoria'),
]

TASKS_STATUS = [
    ('AB','Aberta'),
    ('EA','Em Andamento'),
    ('CA','Cancela'),
    ('CO','Concluída'),
    ('EN','Encerrada'),
]

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    environmentFK = models.ForeignKey(Environments, related_name='tasksEnvironments', on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name='tasksCustomUser', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=100,choices=TASKS_TYPE)
    status = models.CharField(max_length=100,choices=TASKS_STATUS)
    # environmentAlocationFK = models.ForeignKey(EnvironmentAlocation, related_name='tasksEnvironmentAlocation', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class TasksAssignees(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksAssigneesTask', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='tasksAssignees', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskFK.title
    
class Equipments(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    assigneeFK = models.ForeignKey(CustomUser, related_name='equipmentsCustomUser', on_delete=models.CASCADE, 
                                   blank=True, null=True)
    
    def __str__(self):
        return self.name

class TasksStatus(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksAssigneesTaskk', on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=TASKS_STATUS)
    creationDate = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.taskFK.title

# FILE_TYPE = [
#     ('D','Document'),
#     ('P', 'Photo')
# ]

    
class TasksEquipments(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksEquipmentssTask', on_delete=models.CASCADE)
    equipmentFK = models.ForeignKey(Equipments, related_name='tasksEquipmentsEquipmentt', on_delete=models.CASCADE)   

    def __str__(self):
        return self.taskFK.name

class FilesTasksStatus(models.Model):
    equipamentFK = models.ForeignKey(TasksEquipments,related_name='fileTasksStatusEquipamentFk',on_delete=models.CASCADE)
    taskStatusFK = models.ForeignKey(TasksStatus, related_name='filesTasksStatusTask', on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    # fileType = models.CharField(max_length=300, choices=FILE_TYPE)

    def __str__(self):
        return self.taskStatusFK.taskFK.name
    
class EnviromentsAssignees(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='enviromentsAssigneesEnvironment', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='enviromentsAssigneesCustomUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.environmentFK.name

class Themes(models.Model):
    name = models.CharField(max_length=100)
    timeLoad = models.IntegerField()

    def __str__(self):
        return self.name

CATEGORY_LIST = [
    ('CAI', 'Curso de Aprendizagem Industrial'),
    ('CT', 'Curso Técnico'),
    ('CST', 'Custo Superior'),
    ('FIC', 'FalleN')
]

DURATION_LIST = [
    ('H','Horas'),
    ('S','Semestre')
]

AREA_LIST = [
    ('TI', 'Tecnologia da Informação'),
    ('MEC', 'Mecanica'),
    ('ElÉTRIC', 'Elétrica')
]

MODALITY_LIST = [
    ('EAD', 'Ensino a Distância'),
    ('PRE', 'Presencial'),
    ('HIB', 'Hibrido')
]

class Courses(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100,choices=CATEGORY_LIST)
    duration = models.IntegerField()
    durationType = models.CharField(max_length=100, choices=DURATION_LIST)
    area = models.CharField(max_length=100, choices=AREA_LIST)
    modality = models.CharField(max_length=100, choices=MODALITY_LIST)
    # themes = models.ManyToManyField(Themes)

    def __str__(self):
        return self.name

class CoursesThemes(models.Model):
    curseFK = models.ForeignKey(Courses, related_name='coursesThemesCourse', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Themes, related_name='coursesThemesTheme', on_delete=models.CASCADE)

    def __str__(self):
        return self.ThemesCourse.curseFK

class Classes(models.Model):
    name = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    courseFK = models.ForeignKey(Courses, related_name='course_class',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ClassesDivision(models.Model):
    name = models.CharField(max_length=100)
    classFK = models.ForeignKey(Classes, related_name='classFKClassesDivision',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TeachersAlocation(models.Model):
    classFK = models.ForeignKey(Classes, related_name='teacherAlocationClassFK', on_delete=models.CASCADE)
    ThemeFK = models.ForeignKey(Themes, related_name='teacherAlocationThemeFK1', on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name='teacherAlocationReporterFkK', on_delete=models.CASCADE)

    def __str__(self):
        return self.classFK.name

AlOCATION_STATUS = [
    ('1','Rascunho'),
    ('2','Assinalado'),
    ('3', 'Concluido')
]

class TeacherAlocationDetail(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    alocationStatus = models.CharField(max_length=100, choices=AlOCATION_STATUS, default='1')
    CustomUserFK = models.ForeignKey(CustomUser,related_name='teacherAlocationDetailCustomUserFK', on_delete=models.CASCADE)
    classDivisionFK = models.ForeignKey(ClassesDivision, related_name='teachetAlocationDetailClassDivisionFK', on_delete=models.CASCADE)

    def __str__(self):
        return self. alocationStatus


WEEK_DAYS = [
    ('Seg','Segunda-Feira'),
    ('Ter','Terça-Feira'),
    ('Qua','Quarta-Feira'),
    ('Qui','Quinta-Feira'),
    ('Sex','Sexta-Feira'),
    ('Sab','Sabado'),
    ('Dom','Domingo')
]

class TeacherAlocationDetailEnv(models.Model):
    weekDay = models.CharField(max_length=30, choices=WEEK_DAYS)
    hourStart = models.TimeField()
    hourEnd = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    enviromentFK = models.ForeignKey(Environments, related_name='teacherAlocationDetailEnviromentFK', on_delete=models.CASCADE)
    teacherAlocationDetailFK = models.ForeignKey(TeacherAlocationDetail, related_name='teacherAlocationDetailFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.weekDay

class Deadline(models.Model):
    targetDate = models.DateField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORY_LIST)

    def __str__(self):
        return self.category

class Signatures(models.Model):
    ownerFK = models.ForeignKey(CustomUser, related_name='signaturesCustomUserFk', on_delete=models.CASCADE)
    Signature = models.CharField(max_length=200)
    creationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ownerFK.name

STATUS_LIST = [
    ('0','Cancelado'),
    ('1','Pendente'),
    ('2','Em Aprovação'),
    ('3','Aprovado'),
    ('4','Em Revisão')
]

class Plan(models.Model):
    CustomUserFK = models.ForeignKey(CustomUser, related_name='planCustomUserFK',on_delete=models.CASCADE)
    CoursesThemesFK = models.ForeignKey(CoursesThemes, related_name='planCursesThemesFK',on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_LIST, default='1')
    signatureFK = models.ForeignKey(Signatures, related_name="planSignatureFK",on_delete=models.CASCADE, blank=True, null=True)
    approverFK = models.ForeignKey(CustomUser, related_name='planApproverFK',on_delete=models.CASCADE, blank=True, null=True)


class PlanStatus(models.Model):
    planFK = models.ForeignKey(Plan, related_name='planStatusPlanFK',on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_LIST)
    comment = models.CharField(max_length=500)
    file = models.CharField(max_length=200)

    def __str__(self):
        return self.planFK.email






