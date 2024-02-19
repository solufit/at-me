"""Add Tasks

Revision ID: 1b58bf3bc3f3
Revises: 4042e27e2f06
Create Date: 2024-02-19 03:06:30.989516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1b58bf3bc3f3'
down_revision: Union[str, None] = '4042e27e2f06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('calendar', 'localID')
    op.add_column('taskList', sa.Column('kind', sa.TEXT(), nullable=True))
    op.add_column('taskList', sa.Column('title', sa.TEXT(), nullable=True))
    op.add_column('taskList', sa.Column('updated', sa.TIMESTAMP(), nullable=True))
    op.add_column('taskList', sa.Column('selfLink', sa.TEXT(), nullable=True))
    op.add_column('taskList', sa.Column('etag', sa.TEXT(), nullable=True))
    op.alter_column('taskList', 'localId',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.add_column('tasks', sa.Column('note', sa.TEXT(), nullable=True))
    op.add_column('tasks', sa.Column('etag', sa.TEXT(), nullable=True))
    op.add_column('tasks', sa.Column('updated', sa.TIMESTAMP(), nullable=True))
    op.add_column('tasks', sa.Column('selfLink', sa.TEXT(), nullable=True))
    op.add_column('tasks', sa.Column('parent', sa.TEXT(), nullable=True))
    op.add_column('tasks', sa.Column('position', sa.TEXT(), nullable=True))
    op.add_column('tasks', sa.Column('status', sa.TEXT(), nullable=True))
    op.add_column('tasks', sa.Column('due', sa.Date(), nullable=True))
    op.add_column('tasks', sa.Column('completed', sa.TIMESTAMP(), nullable=True))
    op.add_column('tasks', sa.Column('deleted', sa.BOOLEAN(), nullable=True))
    op.add_column('tasks', sa.Column('hidden', sa.BOOLEAN(), nullable=True))
    op.alter_column('tasks', 'id',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('tasks', 'kind',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.drop_constraint('tasks_localId_fkey', 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'localId')
    op.drop_column('tasks', 'description')
    op.drop_column('tasks', 'duetime')
    op.alter_column('users', 'localId',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.drop_column('worktimeDate', 'localID')
    op.drop_column('worktimeWeek', 'localID')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('worktimeWeek', sa.Column('localID', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('worktimeDate', sa.Column('localID', sa.TEXT(), autoincrement=False, nullable=True))
    op.alter_column('users', 'email',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=30),
               existing_nullable=True)
    op.alter_column('users', 'localId',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
    op.add_column('tasks', sa.Column('duetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('tasks', sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('tasks', sa.Column('localId', sa.VARCHAR(length=25), autoincrement=False, nullable=True))
    op.create_foreign_key('tasks_localId_fkey', 'tasks', 'users', ['localId'], ['localId'])
    op.alter_column('tasks', 'kind',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)
    op.alter_column('tasks', 'id',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
    op.drop_column('tasks', 'hidden')
    op.drop_column('tasks', 'deleted')
    op.drop_column('tasks', 'completed')
    op.drop_column('tasks', 'due')
    op.drop_column('tasks', 'status')
    op.drop_column('tasks', 'position')
    op.drop_column('tasks', 'parent')
    op.drop_column('tasks', 'selfLink')
    op.drop_column('tasks', 'updated')
    op.drop_column('tasks', 'etag')
    op.drop_column('tasks', 'note')
    op.alter_column('taskList', 'localId',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)
    op.drop_column('taskList', 'etag')
    op.drop_column('taskList', 'selfLink')
    op.drop_column('taskList', 'updated')
    op.drop_column('taskList', 'title')
    op.drop_column('taskList', 'kind')
    op.add_column('calendar', sa.Column('localID', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
