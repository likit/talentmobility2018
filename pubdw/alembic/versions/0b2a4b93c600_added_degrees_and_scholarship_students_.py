"""Added degrees and scholarship students tables

Revision ID: 0b2a4b93c600
Revises: 2ed3ec5b717d
Create Date: 2018-05-30 16:45:59.350550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2a4b93c600'
down_revision = '2ed3ec5b717d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('degrees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scholarship_students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('field_of_study', sa.String(), nullable=True),
    sa.Column('specialty', sa.String(), nullable=True),
    sa.Column('degree_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['degree_id'], ['degrees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scholarship_students')
    op.drop_table('degrees')
    # ### end Alembic commands ###
