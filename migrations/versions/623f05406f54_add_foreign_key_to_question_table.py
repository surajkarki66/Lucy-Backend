"""add foreign key to question table

Revision ID: 623f05406f54
Revises: 0b0019eeacd4
Create Date: 2022-05-25 19:57:07.946841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623f05406f54'
down_revision = '0b0019eeacd4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('questions', sa.Column('intent', sa.String(100), nullable=False))
    op.create_foreign_key('question_intents_fk', source_table="questions", referent_table="intents", local_cols=[
                          'intent'], remote_cols=['intent'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('question_intents_fk', table_name="questions")
    op.drop_column('questions', 'intent')
