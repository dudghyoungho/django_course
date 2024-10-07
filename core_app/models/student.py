from django.db import models

from core_app.models.person import Person


class Student(Person):
    student_id = models.CharField(max_length=10, verbose_name="학번")
    department = models.ForeignKey("core_app.department", on_delete=models.PROTECT)

    class Meta:
        db_table = 'student'
        verbose_name = '학생'
