from django.test import TestCase

# Create your tests here.
import uuid


for i in range(20):
    myid = uuid.uuid4()
    print(myid)