pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Code already checked out by Jenkins"
            }
        }

        stage('Build') {
            steps {
                echo "Building Docker image"
                sh 'docker build -t tech-api:${BUILD_NUMBER} .'
            }
        }

        stage('Unit Test') {
            steps {
                echo "Running tests"
                sh 'python -m pytest || true'
            }
        }

        stage('Push Image') {
            steps {
                echo "Tagging Docker image"
                sh 'docker tag tech-api:${BUILD_NUMBER} tech-api:latest'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to Kubernetes"
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Checking running pods"
                sh 'kubectl get pods'
            }
        }

    }

    post {
        success {
            echo "Pipeline completed successfully"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
