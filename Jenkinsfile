pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "🔨 Building Docker image..."
                    sh 'docker build -t sentiment-app:latest .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "🚀 Running container..."
                    // Stop old container if it exists
                    sh 'docker stop sentiment-container || true && docker rm sentiment-container || true'
                    // Run new container
                    sh 'docker run -d -p 5000:5000 --name sentiment-container sentiment-app:latest'
                }
            }
        }

        stage('Verify') {
            steps {
                script {
                    echo "✅ Checking running containers..."
                    sh 'docker ps'
                }
            }
        }
    }
}
