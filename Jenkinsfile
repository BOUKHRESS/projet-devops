pipeline {
    agent any

    environment {
        APP_PORT = '5001'
        PROM_PORT = '9091'
        GRAFANA_PORT = '3001'
    }

    stages {

        stage('Verification') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
                sh 'docker --version'
                sh 'docker compose version'
            }
        }

        stage('Test Python') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Docker Compose') {
            steps {
                sh '''
                    docker compose down -v || true
                    docker compose up -d --build
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    sleep 10

                    docker compose ps

                    docker compose exec -T python-app python3 -c \
                    "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/').read().decode())"

                    docker compose exec -T python-app python3 -c \
                    "import urllib.request; data=urllib.request.urlopen('http://127.0.0.1:5000/metrics').read().decode(); print(data); assert 'app_requests_total' in data"
                '''
            }
        }

        stage('Fin') {
            steps {
                echo 'CI/CD Jenkins + Docker Compose terminé avec succès !'
            }
        }
    }

    post {
        always {
            sh 'docker compose down -v || true'
        }
    }
}
