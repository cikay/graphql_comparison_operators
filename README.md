Build

`docker-compose build`

Run

`docker-compose up`

Go to `http://0.0.0.0:8000/graphql`

Create a task

```graphql
mutation{
  createTask(
    task: {
      content: "first task"
    }
  ){
    id
  }
}
```

Query tasks

```graphql
{
  tasks(
    query: {
      createdAt: {
      	gt: "2023-06-19T12:21:35.640+00:00"
    	}
    }
  ){
    id
  }
}
```
