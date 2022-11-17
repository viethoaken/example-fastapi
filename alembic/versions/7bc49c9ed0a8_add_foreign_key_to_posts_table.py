"""add foreign-key to posts table

Revision ID: 7bc49c9ed0a8
Revises: adbc33572b66
Create Date: 2022-11-16 23:12:41.035489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bc49c9ed0a8'
down_revision = 'adbc33572b66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', 
                            local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('poss_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
