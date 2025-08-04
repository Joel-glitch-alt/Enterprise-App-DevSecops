pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    environment {
        SONARQUBE = 'Jenkins-sonar-server'
    }

    stages {
        stage("Install Dependencies") {
            steps {
                sh '''
                    apt-get update && apt-get install -y openjdk-17-jre-headless
                    pip install pytest pytest-cov
                '''
            }
        }

        stage("Run Python Script") {
            steps {
                sh 'python main.py'
            }
        }

        stage("Run Tests with Coverage") {
            steps {
                sh '''
                    pytest --maxfail=1 --disable-warnings -q \
                        --junitxml=pytest-report.xml \
                        --cov=. --cov-report=xml
                '''
            }
        }

        stage("SonarQube Analysis") {
            steps {
                script {
                    def sonarScannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv("${SONARQUBE}") {
                        sh """
                            ${sonarScannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=enterprise_appp \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=$SONAR_HOST_URL \
                            -Dsonar.login=$SONAR_AUTH_TOKEN \
                            -Dsonar.python.version=3.10 \
                            -Dsonar.junit.reportPaths=pytest-report.xml \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.exclusions=**/*test*/**,**/__pycache__/**
                        """
                    }
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            junit 'pytest-report.xml'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}