pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        echo 'Cloning repo...'
      }
    }

    stage('Run Python') {
      steps {
        sh 'python3 pattern.py'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying app...'
      }
    }
  }
  post {
    success {
      echo '✅ Pipeline succeeded!'
    }
    failure {
      echo '❌ Pipeline failed!'
    }
    always {
      echo '🔁 Pipeline finished!!!'
    }
  }
}
