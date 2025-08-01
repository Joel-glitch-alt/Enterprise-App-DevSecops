// pipeline {
//     agent {
//         docker {
//             image 'python:3.10'
//         }
//     }

//         environment {
//             SONARQUBE = 'Jenkins-sonar-server'
//         }

//     stages {
//         stage("Install Dependencies") {
//             steps {
//                 sh 'pip install pytest'
//             }
//         }

//         stage("Run Python Script") {
//             steps {
//                 sh 'python main.py'
//             }
//         }

//         stage("Run Tests with Pytest") {
//             steps {
//                 sh 'pytest --maxfail=1 --disable-warnings -q'
//             }
//         }
//           stage('SonarQube Analysis') {
//             steps {
//                 withSonarQubeEnv("${SONARQUBE}") {
//                     sh 'mvn sonar:sonar'
//                 }
//             }
//         }
        
//     }
// }

pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    
    environment {
        SONARQUBE = 'Jenkins-sonar-server'
        SCANNER_HOME = tool 'SonarQubeScanner'
    }
    
    stages {
        stage("Install Dependencies") {
            steps {
                sh '''
                    pip install pytest
                    pip install pytest-cov
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
                sh '''
                    pytest --maxfail=1 --disable-warnings -q \
                           --cov=. --cov-report=xml --cov-report=html
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh '''
                        ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=python-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_AUTH_TOKEN} \
                        -Dsonar.python.coverage.reportPaths=coverage.xml
                    '''
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
    
    post {
        always {
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