import uuid

class Helpers:
    @staticmethod
    def generate_random_email():
        unique_id = uuid.uuid4().hex[:8]
        return f"sultan_test_{unique_id}@yandex.ru"