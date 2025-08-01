
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
                    # Install Java (required for SonarQube Scanner)
                    apt-get update && apt-get install -y openjdk-17-jre-headless
                    pip install pytest
                '''
            }
        }

        stage("Run Python Script") {
            steps {
                sh 'python main.py'
            }
        }

        stage("Run Tests with Pytest") {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q --junitxml=pytest-report.xml'
            }
        }

        stage("SonarQube Analysis") {
            steps {
                script {
                    // Get the SonarScanner tool
                    def sonarScannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv("${SONARQUBE}") {
                        sh """
                            ${sonarScannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=enterprise_appp \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=$SONAR_HOST_URL \
                            -Dsonar.login=$SONAR_AUTH_TOKEN \
                            -Dsonar.python.version=3.10 \
                            -Dsonar.junit.reportPaths=pytest-report.xml
                        """
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Publish test results using correct method
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

