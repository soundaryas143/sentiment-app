pipeline {
    agent any

    environment {
        APP_NAME = "sentiment-app"
        IMAGE_NAME = "sentiment-app:latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Container') {
            steps {
                echo "Running container..."
                // Stop old container if already running
                sh "docker rm -f ${APP_NAME} || true"
                // Run new container on port 5002
                sh "docker run -d -p 5002:5002 --name ${APP_NAME} ${IMAGE_NAME}"
            }
        }
    }
}
