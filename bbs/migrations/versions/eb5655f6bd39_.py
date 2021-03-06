"""empty message

Revision ID: eb5655f6bd39
Revises: 5c189547133e
Create Date: 2020-06-09 15:25:55.207945

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eb5655f6bd39'
down_revision = '5c189547133e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('_password', sa.String(length=200), nullable=True))
    op.drop_column('cms_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('password', mysql.VARCHAR(length=50), nullable=True))
    op.drop_column('cms_user', '_password')
    # ### end Alembic commands ###
