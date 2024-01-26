pipeline {
    agent any
    
    parameters {
        string(name: 'User', description: 'Enter name of User')
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                script {
                   git branch: 'main', credentialsId: 'Github', url: 'git@github.com:omeshvalyal/Encrypted-Package.git'
                }
            }
        }

        stage('Generate Package') {
            steps {
                script {
                    sh "python3 ${workspace}/download.py"
                }
            }
        }
        stage('Calculate sha512sum of Package') {
            steps {
                script {
                    def sha512Sum = sh(script: "shasum -a 512 ${app_package} | awk '{print \$1}'", returnStdout: true).trim()
                    echo "SHA-512 Sum: ${sha512Sum}"
                }
            }
        }
        stage('Generate Random Password') {
            steps {
                script {
                    def randomPassword = sh(script: 'pwgen -1 12', returnStdout: true).trim()
                    echo "Random Password: ${randomPassword}"
                }
            }
        }
    }
}
