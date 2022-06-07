"""create feedback table

Revision ID: 6341cb79c0d7
Revises: 
Create Date: 2022-06-07 20:14:36.594974

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '6341cb79c0d7'
down_revision = None
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

