"""add user table

Revision ID: adbc33572b66
Revises: fe3b12a57074
Create Date: 2022-11-16 22:42:10.807187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adbc33572b66'
down_revision = 'fe3b12a57074'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False),
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
