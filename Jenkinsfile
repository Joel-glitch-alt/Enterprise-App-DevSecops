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
    }

    tools {
        // This requires SonarScanner plugin to be installed on Jenkins
        // and SonarScanner to be configured in Global Tool Configuration
        sonarScanner 'sonar-scanner'
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
                sh 'pytest --maxfail=1 --disable-warnings -q --junitxml=pytest-report.xml'
            }
        }

        stage("SonarQube Analysis") {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=python_project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONAR_HOST_URL \
                        -Dsonar.login=$SONAR_AUTH_TOKEN \
                        -Dsonar.python.version=3.10 \
                        -Dsonar.junit.reportPaths=pytest-report.xml
                    '''
                }
            }
        }
    }
}