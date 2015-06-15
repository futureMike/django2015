from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.

class Join(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    MARTIAN_WAR = 'MW'
    INTERSTELLAR_TRAVEL = 'IT'
    FLEEING_JUSTICE = 'FJ'
    MEET_CHICKS = 'MC'
    
    JOIN_REASON = (
        (MARTIAN_WAR, 'Martian_War'),
        (INTERSTELLAR_TRAVEL, 'Interstellar Travel'),
        (FLEEING_JUSTICE, 'Fleeing Justice'),
        (MEET_CHICKS, 'Meet Chicks'),
        
    )
    join_reason = models.CharField(max_length=2, choices=JOIN_REASON, default=MARTIAN_WAR)
    
    def __unicode__(self):
        return smart_unicode(self.email)
