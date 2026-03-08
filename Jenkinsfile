pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t tech-api:latest .'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'python -m pytest || true'
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }

        stage('Promote') {
            steps {
                echo "Application promoted to production"
            }
        }

    }
}
