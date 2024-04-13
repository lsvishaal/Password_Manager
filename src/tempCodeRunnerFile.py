def authenticate_with_uuid3(self, namespace, name):
    uuid3 = uuid.uuid3(namespace, name)
    return self.authenticate(str(uuid3))