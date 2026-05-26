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
  }
}
