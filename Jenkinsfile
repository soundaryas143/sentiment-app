pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "soundaryas1/sentiment-app"
        APP_PORT = "5002"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    COMMIT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh """
                        docker build -t ${DOCKER_IMAGE}:${COMMIT} -t ${DOCKER_IMAGE}:latest .
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${COMMIT}
                        docker push ${DOCKER_IMAGE}:latest
                        docker logout
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh """
                        docker rm -f sentiment-app || true
                        docker run -d --name sentiment-app -p ${APP_PORT}:${APP_PORT} ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }
    }
}
