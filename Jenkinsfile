pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage("Install Dependencies") {
            steps {
                sh 'pip install pytest'
            }
        }

        stage("Run Python Script") {
            steps {
                sh 'python main.py'
            }
        }

        stage("Run Tests with Pytest") {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
