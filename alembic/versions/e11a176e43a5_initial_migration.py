"""Initial migration

Revision ID: e11a176e43a5
Revises: 
Create Date: 2024-08-14 12:24:03.646123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = 'e11a176e43a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    
    if('categories' not in inspector.get_table_names()):
        op.create_table('categories',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('name', sa.String(26), nullable=True),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
       
    if 'movies' not in inspector.get_table_names():
        op.create_table('movies',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('title', sa.String(50), nullable=True),
            sa.Column('description', sa.String(1000), nullable=True),
            sa.Column('duration', sa.Integer(), nullable=True),
            sa.Column('release_date', sa.Date(), nullable=True),
            sa.Column('rating', sa.Float(), nullable=True),
            sa.Column('image', sa.String(500), nullable=True),
            sa.Column('video', sa.String(500), nullable=True),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    if('movie_categories' not in inspector.get_table_names()):
        op.create_table('movie_categories',
            sa.Column('movie_id', sa.Integer(), nullable=False),
            sa.Column('category_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
            sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
            sa.PrimaryKeyConstraint('movie_id', 'category_id'),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    
    if('users' not in inspector.get_table_names()):
        op.create_table('users',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('name', sa.String(16), nullable=True),
            sa.Column('email', sa.String(100), nullable=True),
            sa.Column('hashed_password', sa.String(100), nullable=True),
            sa.Column('is_admin', sa.Boolean(), server_default=sa.text('0'), nullable=True),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
        
    existing_indexes = {index['name'] for index in inspector.get_indexes('categories')}
    if 'ix_categories_name' not in existing_indexes:
        op.create_index('ix_categories_name', 'categories', ['name'], unique=False)
    if 'ix_categories_id' not in existing_indexes:
        op.create_index('ix_categories_id', 'categories', ['id'], unique=False)

    existing_indexes = {index['name'] for index in inspector.get_indexes('users')}
    if 'ix_users_name' not in existing_indexes:
        op.create_index('ix_users_name', 'users', ['name'], unique=False)
    if 'ix_users_email' not in existing_indexes:
        op.create_index('ix_users_email', 'users', ['email'], unique=False)
        
    
    if 'wishlists' not in inspector.get_table_names():
        op.create_table('wishlists',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.Column('movie_id', sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    existing_indexes = {index['name'] for index in inspector.get_indexes('wishlists')}
    if 'ix_wishlists_id' not in existing_indexes:
        op.create_index('ix_wishlists_id', 'wishlists', ['id'], unique=False)
    
    if 'locations' not in inspector.get_table_names():
        op.create_table('locations',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('city', sa.String(30), nullable=True),
            sa.Column('country', sa.String(30), nullable=True),
            sa.Column('place', sa.String(200), nullable=True),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    existing_indexes = {index['name'] for index in inspector.get_indexes('locations')}
    if 'ix_locations_id' not in existing_indexes:
        op.create_index('ix_locations_id', 'locations', ['id'], unique=False)
    if 'ix_locations_country' not in existing_indexes:
        op.create_index('ix_locations_country', 'locations', ['country'], unique=False)
    if 'ix_locations_city' not in existing_indexes:
        op.create_index('ix_locations_city', 'locations', ['city'], unique=False)
    
    if 'theaters' not in inspector.get_table_names():
        op.create_table('theaters',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('name', sa.String(26), nullable=True),
            sa.Column('location_id', sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    existing_indexes = {index['name'] for index in inspector.get_indexes('theaters')}
    if 'ix_theaters_name' not in existing_indexes:
        op.create_index('ix_theaters_name', 'theaters', ['name'], unique=False)
    if 'ix_theaters_id' not in existing_indexes:
        op.create_index('ix_theaters_id', 'theaters', ['id'], unique=False)
    
    
    if 'showtimes' not in inspector.get_table_names():
        op.create_table('showtimes',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('movie_id', sa.Integer(), nullable=True),
            sa.Column('theater_id', sa.Integer(), nullable=True),
            sa.Column('start_time', sa.DateTime(), nullable=True),
            sa.Column('end_time', sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
            sa.ForeignKeyConstraint(['theater_id'], ['theaters.id'], ),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    existing_indexes = {index['name'] for index in inspector.get_indexes('showtimes')}
    if 'ix_showtimes_id' not in existing_indexes:
        op.create_index('ix_showtimes_id', 'showtimes', ['id'], unique=False)
    
    if 'seats' not in inspector.get_table_names():
        op.create_table('seats',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('theater_id', sa.Integer(), nullable=True),
            sa.Column('seat_number', sa.String(16), nullable=True),
            sa.Column('seat_type', sa.String(16), nullable=True),
            sa.ForeignKeyConstraint(['theater_id'], ['theaters.id'], ),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    existing_indexes = {index['name'] for index in inspector.get_indexes('seats')}
    if 'ix_seats_seat_number' not in existing_indexes:
        op.create_index('ix_seats_seat_number', 'seats', ['seat_number'], unique=False)
    if 'ix_seats_id' not in existing_indexes:
        op.create_index('ix_seats_id', 'seats', ['id'], unique=False)
    
    if 'tickets' not in inspector.get_table_names():
        op.create_table('tickets',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.Column('showtime_id', sa.Integer(), nullable=True),
            sa.Column('seat_id', sa.Integer(), nullable=True),
            sa.Column('purchase_date', sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(['seat_id'], ['seats.id'], ),
            sa.ForeignKeyConstraint(['showtime_id'], ['showtimes.id'], ),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
    existing_indexes = {index['name'] for index in inspector.get_indexes('tickets')}
    if 'ix_tickets_id' not in existing_indexes:
        op.create_index('ix_tickets_id', 'tickets', ['id'], unique=False)
    
    if 'wishlist_movie' not in inspector.get_table_names():
        op.create_table('wishlist_movie',
            sa.Column('wishlist_id', sa.Integer(), nullable=False),
            sa.Column('movie_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
            sa.ForeignKeyConstraint(['wishlist_id'], ['wishlists.id'], ),
            sa.PrimaryKeyConstraint('wishlist_id', 'movie_id'),
            mysql_collate='utf8mb4_0900_ai_ci',
            mysql_default_charset='utf8mb4',
            mysql_engine='InnoDB'
        )
            
    ## commands auto generated by Alembic - please adjust! ###
    

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlist_movie')
    op.drop_index('ix_tickets_id', table_name='tickets')
    op.drop_table('tickets')
    op.drop_index('ix_seats_id', table_name='seats')
    op.drop_index('ix_seats_seat_number', table_name='seats')
    op.drop_table('seats')
    op.drop_index('ix_showtimes_id', table_name='showtimes')
    op.drop_table('showtimes')
    # op.drop_table('movies')
    op.drop_index('ix_theaters_id', table_name='theaters')
    op.drop_index('ix_theaters_name', table_name='theaters')
    op.drop_table('theaters')
    op.drop_index('ix_locations_id', table_name='locations')
    op.drop_index('ix_locations_country', table_name='locations')
    op.drop_index('ix_locations_city', table_name='locations')
    op.drop_table('locations')
    op.drop_index('ix_wishlists_id', table_name='wishlists')
    op.drop_table('wishlists')
    op.drop_index('ix_users_email', table_name='users')
    # op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_categories_id', table_name='categories')
    op.drop_index('ix_categories_name', table_name='categories')
    op.drop_table('categories')
    op.drop_table('movie_categories')
    # ### end Alembic commands ###