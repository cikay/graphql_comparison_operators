# GraphQL Comparison Operators

Use comparison operators in GraphQL queries, allowing for more powerful and flexible data filtering capabilities.

# Supported Operators

- `exact`: Equal to
- `iexact`: Case-insensitive equal
- `contains`: String contains
- `icontains`: Case-insensitive string contains
- `in_list`: Included in an array
- `not_in_list`: Not included in an array
- `gt`: Greater than
- `gte`: Greater than or equal to
- `lt`: Less than
- `lte`: Less than or equal to
- `startswith`: String starts with
- `istartswith`: Case-insensitive string starts with
- `endswith`: String ends with
- `iendswith`: Case-insensitive string ends with 
- `regex`: String regex
- `iendswith`: Case-insensitive string regex


## Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/graphql-comparison-operators.git
   cd graphql-comparison-operators
   ```

2. Build the Docker containers:
   ```bash
   docker-compose build
   ```

3. Start the application:
   ```bash
   docker-compose up
   ```

4. Access the GraphQL playground at:
   ```
   http://0.0.0.0:8000/graphql
   ```

### Create a New Task

```graphql
mutation {
  createTask(
    task: {
      content: "first task"
    }
  ) {
    id
    content
    createdAt
  }
}
```

### Query Tasks with Filters

#### Filter by creation date (greater than)

```graphql
{
  tasks(
    query: {
      createdAt: {
        gt: "2023-06-19T12:21:35.640+00:00"
      }
    }
  ) {
    id
    content
    createdAt
  }
}
```

#### Filter with multiple conditions

```graphql
{
  tasks(
    query: {
      createdAt: {
        gte: "2023-06-01T00:00:00.000+00:00",
        lte: "2025-03-03T07:48:11.572456"
      }
    }
  ) {
    id
    content
    createdAt
  }
}
```


## Learn More

For a detailed explanation of how comparison operators work in GraphQL, check out my article:
[Query Operators in GraphQL](https://medium.com/@muzaffer-cikay/query-operators-in-graphql-1453e3b517ad)
