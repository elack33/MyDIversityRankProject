from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Demographics(models.Model):
    demographic = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.demographic


class YearOfBirth(models.Model):
    year = models.CharField(
        max_length=4,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.year


class Genders(models.Model):
    gender = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.gender


class Interests(models.Model):
    interest = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.interest


class Orientations(models.Model):
    orientation = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.orientation


class Careers(models.Model):
    career = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.career


class Relationship(models.Model):
    status = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.status


class Ogamy(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )

    def __unicode__(self):
        return self.title


class Questions(models.Model):
    question = models.TextField(
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        Questions,
        null=False,
        blank=False,
    )
    answer = models.TextField(
        null=False,
        blank=False,
        max_length=65535,
    )


class SurveySetup(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )
    author = models.ForeignKey(
        User,
        null=False,
        blank=False,
    )

    def __unicode__(self):
        return self.name


class SurveyResponses(models.Model):
    author = models.ForeignKey(
        User,
        null=False,
        blank=False
    )
    demographic = models.ForeignKey(
        Demographics,
        null=False,
        blank=False
    )
    year_of_birth = models.ForeignKey(
        YearOfBirth,
        null=False,
        blank=False
    )
    gender = models.ForeignKey(
        Genders,
        null=False,
        blank=False
    )
    interest01 = models.ForeignKey(
        Interests,
        null=False,
        blank=False
    )
    interest02 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i02',
    )
    interest023 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i03',
    )
    interest04 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i04',
    )
    interest05 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i05',
    )
    interest06 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i06',
    )
    interest07 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i07',
    )
    interest08 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i08',
    )
    interest09 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i09',
    )
    interest10 = models.ForeignKey(
        Interests,
        null=True,
        blank=True,
        related_name='i10',
    )
    orientation = models.ForeignKey(
        Orientations,
        null=False,
        blank=False
    )
    career01 = models.ForeignKey(
        Careers,
        null=False,
        blank=False
    )
    career02 = models.ForeignKey(
        Careers,
        null=True,
        blank=True,
        related_name='c02',
    )
    relationship = models.ForeignKey(
        Relationship,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return str(self.pk)

