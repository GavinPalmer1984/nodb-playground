import unittest

from app.users import model

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.ts = 'techsupport@herolfg.com'
        self.gp = 'gavin@herolfg.com'

    def test_save_load_delete_user(self):
        user = model.User()
        user.email = self.gp
        user.name = 'gp'
        user.save()

        user.email = self.ts
        user.name = 'ts'
        user.save()

        user.load(self.ts)
        self.assertEquals(self.ts, user.email)
        user.delete(self.ts)

        user.load(self.gp)
        self.assertEquals(self.gp, user.email)
        user.delete(self.gp)

    def test_save_list_delete_user(self):
        user = model.User()
        user.email = self.gp
        user.name = 'gp'
        user.save()

        user.email = self.ts
        user.name = 'ts'
        user.save()

        users = user.all()
        self.assertEquals(2, len(users))

        for user in users:
            user.delete(user.email)

        users = user.all()
        self.assertEquals(0, len(users))
