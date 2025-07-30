pipeline {
    agent any

    stages {
        stage("Run Python Script") {
            steps {
                sh 'python main.py'
            }
        }
        stage('Run Tests with Pytest') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
