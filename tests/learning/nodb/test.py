import unittest
from nodb import NoDB

from app.users import model

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.nodb = NoDB()
        self.nodb.bucket = 'herolfg-tests-learning-nodb-users' # arn:aws:s3:::herolfg-tests-learning-nodb-users
        self.nodb.index = 'email'
        self.ts = 'techsupport@herolfg.com'
        self.gp = 'gavin@herolfg.com'

    def test_save_load_delete_user(self):
        user = model.User()
        user.email = self.gp
        user.name = 'gp'
        self.nodb.save(user)

        user.email = self.ts
        user.name = 'ts'
        self.nodb.save(user)

        actual = self.nodb.load(self.ts)
        self.assertEquals(self.ts, actual.email)
        self.nodb.delete(self.ts)

        actual = self.nodb.load(self.gp)
        self.assertEquals(self.gp, actual.email)
        self.nodb.delete(self.gp)
