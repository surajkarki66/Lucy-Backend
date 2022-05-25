"""add foreign key to response table

Revision ID: 2570a05785b2
Revises: 623f05406f54
Create Date: 2022-05-25 20:06:25.306439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2570a05785b2'
down_revision = '623f05406f54'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('responses', sa.Column('intent', sa.String(100), nullable=False))
    op.create_foreign_key('response_intents_fk', source_table="responses", referent_table="intents", local_cols=[
                          'intent'], remote_cols=['intent'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('response_intents_fk', table_name="responses")
    op.drop_column('responses', 'intent')
