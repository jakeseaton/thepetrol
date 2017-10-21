from __future__ import unicode_literals
from common import enum
from django.db import models
# from django.contrib.postgres.fields import JSONField, ArrayField

class Color(enum.Enum):
    black = enum.Item(1, "Black")
    brown = enum.Item(2, "Brown")
    orange = enum.Item(3, "Orange")

class AnimalType(enum.Enum):
    dog = enum.Item(1, "Dog")
    cat = enum.Item(2, "Cat")

class Pattern(enum.Enum):
    spotted = enum.Item(1, "Spotted")
    striped = enum.Item(2, "Striped")
    calico = enum.Item(3, "Calido")
    solid = enum.Item(4, "Solid")

class BreedType(enum.Enum):
    # there are < 400 breeds of dog in the world
    goldem_retreiver = enum.Item(1, "Golden Retriever")



class DogBreedGroup(enum.Enum):
    # https://www.psychologytoday.com/blog/canine-corner/201305/how-many-breeds-dogs-are-there-in-the-world


    #Sheepdogs and Cattle Dogs other than Swiss Cattle Dogs (this group includes most of the dogs found classified as "herding dogs" by other kennel clubs).
    herding = enum.Item(1, "Herding")
    # Pinscher and Schnauzer - Molossoid Breeds - Swiss Mountain and Cattle Dogs and Other Breeds (the Molossian breeds include the dogs known as the mastiffs by most other kennel clubs)
    molosser  = enum.Item(2, "Molosser")
    # Terriers
    terrier = enum.Item(3, "Terrier")
    # Dachshunds
    dachsund = enum.Item(4, "Dachsund")
    # Spitz and Primitive Types
    spitz = enum.Item(5, "Spitz")

    # Scenthounds and Related Breeds
    scenthound = enum.Item(6, "Scenthound")
    # Pointers and Setters
    pointer = enum.Item(7, "Pointer")
    # Retrievers - Flushing Dogs - Water Dogs
    retreiver = enum.Item(8, "Retriever")
    # Companion and Toy Dogs
    companion  = enum.Item(9, "Companion")
    # Sighthounds
    sighthound = enum.Item(10, "Sighthound")

class CatBreedGroup(enum.Enum):
    pass


class Size(enum.Enum):
    small = enum.Item(1, "Small")
    medium = enum.Item(2, "Medium")
    large = enum.Item(3, "Large")

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Message(TimeStamp):

    '''
    Represents a message that was sent or received via twilio
    '''

    from_number = models.IntegerField()
    to_number = models.IntegerField()

    # did we send this message
    sent = models.BooleanField(default=False)
    # did we receive this message
    received = models.BooleanField(default=True)

    # was there an error in sending this message
    error = models.BooleanField(default=False)
    # animal = models.ForeignKey(Animal, blank=True, null=True, related_name="messages")
    text = models.CharField(max_length=2048)



class Animal(TimeStamp):


    # has_tag = models.BooleanField()

    # the size of the animal
    # size = models.IntegerField(choices=Size, default=Size.small)
    # color = models.IntegerField(choices=Color, default=Color)
    # animal_type = models.IntegerField(choices=AnimalType)
    # pattern = models.IntegerField(choices=Pattern)
    # breed = models.CharField(max_length=255)
    # breed_type = models.IntegerField(choices=BreedType)
    # dog_breed_group = models.IntegerField(choices=DogBreedGroup, blank=True, null=True)
    # cat_breed_group = models.IntegerField(choices=DogBreedGroup, blank=True, null=True)

    # the phone number that texted this image
    phone_number = models.IntegerField(blank=True, null=True)

    # the image of the animal
    # image = models.ImageField(blank=True, null=True)

    # the geopoint of the image
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # the result of google image processing
    # google_image_result = JSONField(default=dict)

    # the conversation, stored as gField(models.CharField(max_length=4096), default=list)

    # another way to achieve this would be to create a record for every message we wend, and foreign key
    # all of them to the
    # location information


# class RescueCenter(models.Model):
#     pass
#     name = models.CharField()









