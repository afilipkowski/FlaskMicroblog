"""users table

Revision ID: d9cb6553663a
Revises: b6679e1253de
Create Date: 2024-04-01 00:11:03.587180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9cb6553663a'
down_revision = 'b6679e1253de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
