"""create user table

Revision ID: efe22b26ee94
Revises: 6341cb79c0d7
Create Date: 2022-06-07 20:17:32.256386

"""
from alembic import op
import sqlalchemy as sa

from app.main.schemas.schemas import Role

# revision identifiers, used by Alembic.
revision = 'efe22b26ee94'
down_revision = '6341cb79c0d7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(32), nullable=False),
                    sa.Column('last_name', sa.String(32), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('role', sa.Enum(Role),
                              server_default="subscriber"),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False), 
                              
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )



def downgrade():
   op.drop_table('users')