from django.db import models

class Factor(models.Model):
    id = models.AutoField(primary_key=True)
    name_tag = models.CharField(max_length=40)
    desc = models.TextField(blank=True, null=True)
    customerTypeTitle = models.CharField(max_length=40)
    customerTypeCode = models.CharField(max_length=2)
    # cycleDay = models.CharField(max_length=40, null=True)
    customerSubTypeCode = models.CharField(max_length=40)
    # cycleCode = models.CharField(max_length=40, null=True)
    ###BAG CONDITION###
    # uquota = models.CharField(max_length=40, null=True)
    alevel = models.CharField(max_length=1, blank=True,null=True)
    atype = models.CharField(max_length=1, blank=True,null=True)
    cid = models.CharField(max_length=40, blank=True,null=True)
    # rquota = models.CharField(max_length=40, null=True)
    # quota = models.CharField(max_length=40, null=True)
    cstatus = models.CharField(max_length=40, blank=True,null=True)
    pind = models.CharField(max_length=1, blank=True,null=True)
    plantype = models.CharField(max_length=40, blank=True,null=True)
    mname = models.CharField(max_length=40, blank=True,null=True)
    stype = models.CharField(max_length=1, blank=True,null=True)
    oname = models.CharField(max_length=40, blank=True,null=True)

    def __str__(self):
        return ('ID : {0} Name : {1}'.format(self.id,self.name_tag)) 

    class Meta:
        db_table = 'factor'

class BodyTag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    req = models.CharField(max_length=40)

    def __str__(self):
        return ('ID : {0} Name : {1} Req {2}'.format(self.id,self.name,self.req)) 

    class Meta:
        db_table = 'body_tag'

class FactorBodyTag(models.Model):
    id = models.AutoField(primary_key=True)
    factor =  models.ForeignKey(Factor, on_delete=models.CASCADE)
    body =  models.ForeignKey(BodyTag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'factor_body_tag'
    def __str__(self):
        return ('ID : {0} factor : {1} body {2}'.format(self.id,self.factor,self.body)) 
