"""create response table

Revision ID: 0b0019eeacd4
Revises: 9b76df62a531
Create Date: 2022-05-25 19:54:02.091266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b0019eeacd4'
down_revision = '9b76df62a531'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table('responses',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('response', sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              nullable=False, server_default=sa.text('now()')),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('response')
                    )


def downgrade():
    op.drop_table('responses')

