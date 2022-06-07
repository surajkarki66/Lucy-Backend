"""create feedback table

Revision ID: 2d16c3820980
Revises: a7eb1216afb4
Create Date: 2022-06-07 08:43:37.217101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d16c3820980'
down_revision = 'a7eb1216afb4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('feedbacks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('person_name', sa.String(255), nullable=False),
                    sa.Column('message', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False), 
                    sa.PrimaryKeyConstraint('id'),
                    )


def downgrade():
    op.drop_table('feedbacks')
