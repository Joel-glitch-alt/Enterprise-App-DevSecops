pipeline {
    agent any

    stages {
        stage("Build Stage") {
            steps {
                echo "======== Executing Python Script ========"
                sh 'python3 main.py'
            }
        }
        stage('Run Tests') {
            steps {
                echo "======== Running Pytest ========"
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
