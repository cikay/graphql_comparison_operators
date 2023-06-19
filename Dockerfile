FROM python:3.10

RUN pip install pipenv

WORKDIR ./graphql_query_operators

COPY Pipfile Pipfile.lock ./

RUN pipenv install

COPY . ./

EXPOSE 8000

CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
