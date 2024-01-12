from django.db import models

class Routes(models.Model):
	route_number = models.CharField(max_length=4)
	route_directions = models.CharField(max_length=255)
	def __str__(self):
		return str(self.route_number)


