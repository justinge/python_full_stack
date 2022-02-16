"""empty message

Revision ID: c8cfc8195884
Revises: 53b587f3e105
Create Date: 2019-06-28 12:13:38.968402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8cfc8195884'
down_revision = '53b587f3e105'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_authors', sa.Column('sex', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_authors', 'sex')
    # ### end Alembic commands ###
