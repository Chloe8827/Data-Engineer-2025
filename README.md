# Data-Engineer-2025# github + docker + postgres

after creating a github repo:

create codespace and using personal vscode

### Install terraform

https://developer.hashicorp.com/terraform/install

```bash
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```



### Remove the existing container

```bash
docker stop pg-database
docker rm pg-database
```

### Create a Docker Network

First, create a custom network to allow your containers to communicate:

```bash
docker network create pg-network
```

### Run PostgreSQL Container

Run the PostgreSQL container with the following command:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v dtc_postgres_volume_local:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
```

- Create a PostgreSQL container with version 13
- Set up environment variables for user, password, and database name
- Mount a volume for persistent storage
- Map port 5432 to your host
- Connect it to the pg-network
- Name the container "pg-database"

### Run pgAdmin Container

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4
```

- Create a pgAdmin container
- Set up environment variables for login
- Map port 8080 to your host
- Connect it to pg-network
- Name the container "pgadmin"

### Access pgAdmin in Your Browser

1. Open your web browser and navigate to http://127.0.0.1:8080
2. Log in with:
   - Email: admin@admin.com
   - Password: root

### Add PostgreSQL Server in pgAdmin

1. Right-click on "Servers" in the left sidebar and select "Register" > "Server"
2. On the "General" tab, give your server a name (e.g., "PostgreSQL Docker")
3. On the "Connection" tab, enter:
   - Host name/address: `pg-database` (this is the name of your PostgreSQL container)
   - Port: `5432`
   - Maintenance database: `ny_taxi` (or "postgres" if you prefer)
   - Username: `root`
   - Password: `root`
4. Click "Save"

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi 
```



# Docker

why we need docker?

1. Local experiment: packages everything it needs to run into one container, so it works the same way on any computer.
2. Integration tests(CI/CD): everyone has the exact same test environment, making results reliable and consistent.
3. Reproducibility: When working on team projects, Docker eliminates the "it works on my machine" problem since everyone uses identical environments.
4. Running pipeline on the cloud (AWS, Kubernetes): Docker makes it easy to deploy and scale applications without worrying about different server configurations.
5. Spark: Docker helps create consistent processing environments across different machines.
6. Serverless functions (like AWS Lambda): Docker can standardize development and testing environments before deployment.

Docker is like a **shipping container** for software - it packages everything needed to run your code in one portable unit that works the same everywhere.

 [docker_cheatsheet.pdf](docker_cheatsheet.pdf) 

[Docker + SQL](https://docs.google.com/document/u/1/d/e/2PACX-1vRJUuGfzgIdbkalPgg2nQ884CnZkCg314T_OBq-_hfcowPxNIA0-z5OtMTDzuzute9VBHMjNYZFTCc1/pub)



