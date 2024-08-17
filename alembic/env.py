
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool, create_engine, text
from alembic import context
from sqlalchemy.exc import OperationalError



from database import Base  

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata

def create_database_if_not_exists(url):
    
    db_name = url.split('/')[-1]
    server_url = url.replace(f'/{db_name}', '')
    engine = create_engine(server_url)
    conn = engine.connect()
    conn.execution_options(isolation_level="AUTOCOMMIT")
    try:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}`"))
        print(f"Database '{db_name}' created or already exists.")
    except OperationalError as e:
        print(f"Error creating database '{db_name}': {e}")
    finally:
        conn.close()


def run_migrations_offline():
    """Izvrši migracije u 'offline' načinu rada."""
    url = config.get_main_option("sqlalchemy.url")
    create_database_if_not_exists(url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Izvrši migracije u 'online' načinu rada."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    url = config.get_main_option("sqlalchemy.url")
    create_database_if_not_exists(url)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
