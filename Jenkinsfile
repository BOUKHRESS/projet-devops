
pipeline {
    agent any

    stages {

        stage('Verification') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Test Python') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Fin') {
            steps {
                echo 'Pipeline CI/CD terminée avec succès !'
            }
        }
    }
}
