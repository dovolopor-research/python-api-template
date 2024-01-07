export PROJECT_NAME="python-api-template"

echo "${PROJECT_NAME} building..."
docker build -t $PROJECT_NAME .
echo "${PROJECT_NAME} build success"