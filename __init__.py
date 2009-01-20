from django.conf import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


db_engine = create_engine(settings.DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=db_engine))


# middleware for running session cleanup code
class Middleware:
    def process_response(self, request, response):
        db_session.remove()
        return response
