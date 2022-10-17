alembic upgrade head
if [ -n "${SEED}" ]; then
  inv seed
fi