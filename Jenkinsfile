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
                sh '''
                    docker rm -f python-app-ci >/dev/null 2>&1 || true

                    docker run -d \
                      --name python-app-ci \
                      projet-devops:jenkins

                    sleep 3

                    docker exec python-app-ci python3 -c \
                      "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/').read().decode())"

                    docker exec python-app-ci python3 -c \
                      "import urllib.request; data=urllib.request.urlopen('http://127.0.0.1:5000/metrics').read().decode(); print(data); assert 'app_requests_total' in data"

                    docker rm -f python-app-ci
                '''
            }
        }

        stage('Fin') {
            steps {
                echo 'CI/CD Flask + Docker + Prometheus terminée avec succès !'
            }
        }
    }
}
