pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm my-python-app'
            }
        }
    }

    post {
        success {
            echo '✅ Docker pipeline success!'
        }
        failure {
            echo '❌ Docker pipeline failed!'
        }
    }
}
