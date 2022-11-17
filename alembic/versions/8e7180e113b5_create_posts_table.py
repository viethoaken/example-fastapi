"""create posts table

Revision ID: 8e7180e113b5
Revises: 
Create Date: 2022-11-16 21:17:42.002160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e7180e113b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                                        sa.Column('title', sa.String(), nullable=False)
    )
    
    pass


def downgrade():
    op.drop_table('posts')
    pass
