// Jenkinsfile

pipeline {
  agent any

  environment {
    // Define your environment variables here
    EC2_HOST = '100.26.146.205'
    EC2_USER = 'ubuntu'
    EC2_KEY_PATH = './DjangoCrud.pem'
    REMOTE_APP_DIR = '/home/ubuntu'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build and Test') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
        sh 'python manage.py test'
      }
    }

    stage('Deploy to AWS EC2') {
      steps {
        script {
          // Copy application files to EC2
          sh "scp -i ${EC2_KEY_PATH} -o StrictHostKeyChecking=no -r . ${EC2_USER}@${EC2_HOST}:${REMOTE_APP_DIR}"

          // SSH into EC2 and restart the application (adjust this according to your deployment process)
          sshCommand remote: [
            host: EC2_HOST,
            user: EC2_USER,
            identityFile: EC2_KEY_PATH
          ], command: "cd ${REMOTE_APP_DIR} && ./restart_script.sh"
        }
      }
    }
  }
}
