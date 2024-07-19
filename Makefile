run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@ PTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PTHONPATH=$PYTHONPATH:$(pwd) alembic upgrede head