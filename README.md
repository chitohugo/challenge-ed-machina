## Challenge for EdMachina

### Running with docker

#### Pre-requisites:
- docker
- docker compose

#### Steps:
1. Create a file called `.env` with environment variables in the root of the project
2. Build with `docker compose build`
3. Run with `docker compose up`
4. In another terminal run the migrations `docker compose exec app alembic upgrade head`

#### How to use: 
- Go to `http://localhost:8000/docs`
- You can also test the endpoints with your preferred rest client. (Postman/Insomnia)

#### Environment Variables (.env)
```
ENV=dev
DATABASE_PORT=5432
POSTGRES_PASSWORD=challenge2023
POSTGRES_USER=postgres
POSTGRES_DB=ed-machina
POSTGRES_HOST=postgres
POSTGRES_HOSTNAME=db
ENGINE=postgresql
```