from django.test import TestCase
from django.contrib.auth.models import User
from .models import Room, Message
from django.utils.text import slugify


class RoomModelTest(TestCase):
    def setUp(self):
        self.room_name = "Test Room"
        self.room = Room.objects.create(name=self.room_name)

    def test_room_creation(self):
        self.assertEqual(self.room.name, self.room_name)

    def test_room_slug_creation(self):
        self.room.save()
        self.assertEqual(self.room.slug, slugify(self.room_name))

    def test_room_str_representation(self):
        self.assertEqual(str(self.room), self.room_name)


class MessageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'testpassword'
        )
        self.room = Room.objects.create(name="Test Room")
        self.message_content = "This is a test message."
        self.message = Message.objects.create(
            room=self.room,
            user=self.user,
            content=self.message_content
        )

    def test_message_creation(self):
        self.assertEqual(self.message.room, self.room)
        self.assertEqual(self.message.user, self.user)
        self.assertEqual(self.message.content, self.message_content)

    def test_message_ordering(self):
        second_message = Message.objects.create(
            room=self.room,
            user=self.user,
            content="Second test message."
        )
        messages = list(Message.objects.all())
        self.assertTrue(
            messages.index(self.message) < messages.index(second_message)
        )
