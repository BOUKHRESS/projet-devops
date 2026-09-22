pipeline {
    agent any

    stages {

        stage('Verification') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
                sh 'docker --version'
            }
        }

        stage('Test Python') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t projet-devops:jenkins .'
            }
        }

        stage('Test Docker') {
            steps {
                sh 'docker run --rm projet-devops:jenkins'
            }
        }

        stage('Fin') {
            steps {
                echo 'CI/CD Docker terminée avec succès !'
            }
        }
    }
}
