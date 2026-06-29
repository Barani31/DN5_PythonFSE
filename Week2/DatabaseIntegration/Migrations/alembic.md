Install

pip install alembic

Initialize

alembic init alembic

Create Migration

alembic revision --autogenerate

Upgrade

alembic upgrade head

Downgrade

alembic downgrade -1