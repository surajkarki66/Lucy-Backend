"""create intent table

Revision ID: 0dcb0e7fa7b6
Revises: 
Create Date: 2022-05-25 19:06:37.224204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dcb0e7fa7b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('intents',
                    sa.Column('intent', sa.String(100),  primary_key=True, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
        
                    sa.PrimaryKeyConstraint('intent'),
    )


def downgrade():
    op.drop_table('intents')
