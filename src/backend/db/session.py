# Handle Database.
# Create Database and Migrate.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

from alembic import command
from alembic.config import Config

from src.backend.db.models import Base

class DB:
    def __init__(self, db_url: str, alembic_ini_path: str = "alembic.ini"):
        self.db_url = db_url
        self.engine = create_engine(db_url, echo=False, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        self.alembic_cfg = Config(alembic_ini_path)
        self.alembic_cfg.set_main_option("sqlalchemy.url", self.db_url)

    def create(self):
        """Create tables from Base metadata."""
        Base.metadata.create_all(bind=self.engine)
        print("Tables created successfully.")

    def migrate(self, revision: str = "head"):
        """Apply Alembic migrations to the latest revision or to a specified one."""
        try:
            command.upgrade(self.alembic_cfg, revision)
            print(f"Database migrated to revision: {revision}")
        except Exception as e:
            print("Migration failed:", e)

# Handle Database Connection.
# CRUD Consept and Transaction.

class DBConnection:
    def __init__(self, db_url):
        self.engine = create_engine(db_url, pool_pre_ping=True)
        self.SessionFactory = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        """Returns a new session."""
        return self.SessionFactory()

    def create(self, obj):
        """Insert a new record."""
        session = self.get_session()
        try:
            session.add(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self):
        """Flush and commit pending changes to the DB."""
        session = self.get_session()
        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, obj):
        """Delete a record."""
        session = self.get_session()
        try:
            session.delete(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def query(self, model, filters=None):
        """
        Query records with optional filters.
        `filters` should be a list of SQLAlchemy filter expressions.
        """
        session = self.get_session()
        try:
            query = session.query(model)
            if filters:
                for condition in filters:
                    query = query.filter(condition)
            results = query.all()
            return results
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    

# Using with Depend on FastAPI.
def get_db():
    pass