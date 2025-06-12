docker compose down -v
docker compose build
docker compose up -d
docker network connect rho-bottes-ai rho-bottes-discord-bot-1
docker network inspect rho-bottes-ai