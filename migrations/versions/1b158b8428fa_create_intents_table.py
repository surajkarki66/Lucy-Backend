"""create intents table

Revision ID: 1b158b8428fa
Revises: efe22b26ee94
Create Date: 2022-09-15 18:58:17.945686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b158b8428fa'
down_revision = 'efe22b26ee94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('intents',
                    sa.Column('title', sa.String(255), primary_key=True, nullable=False),
                    sa.Column('intent_no', sa.Integer(), unique=True, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False), 
                    sa.PrimaryKeyConstraint('title'),
                    )

def downgrade() -> None:
    op.drop_table('intents')
