from django.utils.translation import ugettext_lazy as _
from django.db import models


class Sudoku(models.Model):
    puzzle_data = models.CharField(
        _(u'Puzzle Data'),
        max_length=500
    )

    solution_data = models.CharField(
        _(u'Solution Data'),
        max_length=500
    )

    timetaken = models.CharField(
        _(u'Time Taken to Solve'),
        max_length=50
    )

    level = models.CharField(
        _(u'Level'),
        max_length=50
    )

    def __unicode__(self):
        return u"%s" % self.timetaken
