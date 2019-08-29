from django.db import models
from django.db.models import Q

class ProductQuerySet(models.query.QuerySet):
    def Marital(self):
        return self.filter()


    def search(self, query):
        lookups = (Q(Marital__icontains=query) |
                  Q(Education__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_by_id(self, Id):
        qs = self.get_queryset().filter(Id=Id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def Marital(self): #Test2.objects.Marital()
        return self.get_queryset().Marital()

    def search(self, query):
        return self.get_queryset().Marital().search(query)





class Test2(models.Model):
      Id =models.IntegerField(primary_key=True)
      Age =models.IntegerField()
      Job  =models.CharField(max_length=200, default='')
      Marital   =models.CharField(max_length=200, default='')
      Education  =models.CharField(max_length=200, default='')
      Default =models.DecimalField(max_digits=19, decimal_places=10)
      Balance  =models.DecimalField(max_digits=19, decimal_places=10)
      HHInsurance  =models.DecimalField(max_digits=19, decimal_places=10)
      CarLoan  =models.DecimalField(max_digits=19, decimal_places=10)
      Communication  =models.CharField(max_length=200, default='')
      LastContactDay   =models.DecimalField(max_digits=19, decimal_places=10)
      LastContactMonth   =models.CharField(max_length=200, default='')
      NoOfContacts    =models.DecimalField(max_digits=19, decimal_places=10)
      DaysPassed    =models.DecimalField(max_digits=19, decimal_places=10)
      PrevAttempts   =models.DecimalField(max_digits=19, decimal_places=10)
      Outcome  =models.CharField(max_length=200, default='')
      CallStart =models.CharField(max_length=200, default='')
      CallEnd   =models.CharField(max_length=200, default='')
      CarInsurance     =models.DecimalField(max_digits=19, decimal_places=10)

      objects = ProductManager()
      def __str__(self):
          return self.Marital


      @property
      def name(self):
          return self.Marital
