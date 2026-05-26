pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "805019"
        IMAGE_NAME = "my-python-app"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_USERNAME/$IMAGE_NAME .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_USERNAME/$IMAGE_NAME'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm $DOCKER_USERNAME/$IMAGE_NAME'
            }
        }
    }

    post {
        success {
            echo '✅ Image pushed to Docker Hub successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
