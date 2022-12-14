"""added email for user

Revision ID: e31e5fff9706
Revises: fef52812fb31
Create Date: 2022-09-16 15:54:19.068003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e31e5fff9706'
down_revision = 'fef52812fb31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
