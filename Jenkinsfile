pipeline {
    agent any

    environment {
        IMAGE_NAME = "uzzu/tech-api"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/tech-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
