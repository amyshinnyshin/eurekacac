from django.db import models

# Create your models here.
class ConsultationContact(models.Model):
    COLLEGE_PACKAGES = 'college-packages'
    STRIVE = 'strive'
    HOURLY = 'hourly'

    PROGRAM_OPTIONS = [
        (COLLEGE_PACKAGES, 'Applied'),
        (STRIVE, 'Interviews'),
        (HOURLY, 'Rejected'),
    ]

    SEVENTH_EIGHTH = '7th-8th'
    NINTH = '9th'
    TENTH = '10th'
    ELEVENTH = '11th'
    TWELFTH = '12th'

    GRADE_LEVELS = [
        (SEVENTH_EIGHTH, '7th-8th Grade'),
        (NINTH, '9th Grade'),
        (TENTH, '10th Grade'),
        (ELEVENTH, '11th Grade'),
        (TWELFTH, '12th Grade'),
    ]

    parent_name = models.CharField(max_length=100)
    parent_email = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=25, choices=GRADE_LEVELS)
    school_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    programs_and_services = models.CharField(max_length=100, choices=PROGRAM_OPTIONS)
    date_appt = models.DateField()
    how_can_we_help = models.TextField(blank=True)


class ConsultationDateRange(models.Model):
    consultation_contact = models.ForeignKey(ConsultationContact, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

