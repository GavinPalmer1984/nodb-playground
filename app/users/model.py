from nodb import NoDB

class User(object):
    email = None
    name = None

    def __init__(self):
        self.nodb = NoDB()
        self.nodb.bucket = 'herolfg-tests-learning-nodb-users'
        self.nodb.index = 'email'
        self.nodb.human_readable_indexes = True

    def __str__(self):
        return "{ email: '%s', name: '%s' }" % (self.email, self.name)

    def save(self):
        self.nodb.save(self)

    def load(self, email):
        instance = self.nodb.load(email)
        self.email = instance.email
        self.name = instance.name
    
    def delete(self, email):
        self.nodb.delete(email)
    
    def all(self):
        result = []

        bucket = self.nodb.s3.Bucket(self.nodb.bucket)
        for obj in bucket.objects.filter(Prefix=self.nodb.prefix):
            serialized = obj.get()["Body"].read()
            deserialized = self.nodb._deserialize(serialized)
            result.append(deserialized['obj'])

        return result