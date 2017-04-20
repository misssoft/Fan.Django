from django.db import models

# Create your models here.

SCHOOL_PHASE_OPTIONS = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('A', '16 to 18')
)

SCHOOL_TYPE_OPTIONS = (
    ('A', 'Academy'),
    ('M', 'Maintained school'),
    ('I', 'Independent school'),
    ('S', 'Special school'),
    ('C', 'College')
)

OFSTED_RATING_OPTIONS = (
    ('1', 'Outstanding'),
    ('2', 'Good'),
    ('3', 'Requires improvement'),
    ('4', 'Inadequate')
)

RELIGIOUS_OPTIONS = (
    ('N', 'No religious character'),
    ('CE', 'Church of England'),
    ('CA', 'Roman Catholic'),
    ('Me', 'Methodist'),
    ('URC', 'United Reformed Church'),
    ('Q', 'Quaker'),
    ('Mo', 'Moravian'),
    ('Se', 'Seventh Day Adventist'),
    ('O', 'Other Christian'),
    ('Mu', 'Muslim'),
    ('H', 'Hindu'),
    ('B', 'Buddist'),
    ('J', 'Jewish'),
    ('Si', 'Sikh'),
    ('U', 'Unitarian'),
    ('Mul', 'Multifaith')
)

PUPIL_GENDER_OPTIONS = (
    ('M', 'Mixed'),
    ('B', 'Boys'),
    ('G', 'Girls')
)

class School (models.Model):
    name = models.CharField(max_length = 250)
    phase = models.CharField(max_length = 1, choices = SCHOOL_PHASE_OPTIONS)
    type = models.CharField(max_length = 1, choices = SCHOOL_TYPE_OPTIONS)
    ofsted = models.CharField(max_length = 1, choices = OFSTED_RATING_OPTIONS)
    ofstedInspected = models.DateTimeField(auto_now=False)
    religious = models.CharField(max_length = 3, default='N', choices = RELIGIOUS_OPTIONS )
    gender = models.CharField(max_length = 1, default='M', choices = PUPIL_GENDER_OPTIONS)
    address = models.CharField(max_length = 100)
    postcode = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
