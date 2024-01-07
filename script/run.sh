export PROJECT_NAME="python-api-template"
export PORT=9999

echo "${PROJECT_NAME} deploying..."

docker run -d --restart=always \
  --name $PROJECT_NAME \
  -p 9999:9999 \
  -v ./conf/:/app/conf \
  -e ENV=prod \
  $PROJECT_NAME

echo "${PROJECT_NAME} deployed"