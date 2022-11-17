"""add content column to posts table

Revision ID: fe3b12a57074
Revises: 8e7180e113b5
Create Date: 2022-11-16 22:27:55.376629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe3b12a57074'
down_revision = '8e7180e113b5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
