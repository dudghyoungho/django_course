from django.db import models

from core_app.models.person import Person


class Professor(Person):
    employee_id = models.CharField(max_length=10)
    department = models.ForeignKey("core_app.department", on_delete=models.PROTECT)

    class Meta:
        db_table = 'professor'
        verbose_name = '교직원'