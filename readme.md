

inicializar ambiente:
source .venv/bin/activate

desativar:
deactivate

pip install fastapi uvicorn


passar todos pacotes para o requirements
pip freeze > requirements.txt


# run
uvicorn fastapi_ddd.main:app --reload --root-path .