# app/db.py
# Since the periodic tasks would need to store the fetcd to connect to QuestDB. hed quotes, we nee
# Therefore, we create a new file in the app package, called db.py. 
# This file contains the PostgreSQL connection pool engine that will serve as the base for our connections.

from psycopg_pool import ConnectionPool
from app.settings import settings
from sqlalchemy import create_engine

pool = ConnectionPool(
    settings.database_url,
    min_size=1,
    max_size=settings.database_pool_size,
)

engine = create_engine(
    settings.database_url, pool_size=settings.database_pool_size, pool_pre_ping=True
)