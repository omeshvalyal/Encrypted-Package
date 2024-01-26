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
                     // Run Python script and capture its output
                    def my_package = sh(script: "python3 ${workspace}/download.py", returnStdout: true).trim()
                    echo '$my_package'
//                    def my_package = sh(returnStatus: true, script: python3 ${workspace}/download.py)
//                    sh "python3 ${workspace}/download.py"
                }
            }
        }
        stage('Calculate sha512sum of Package') {
            steps {
                script {
                    def sha512Sum = sh(script: "openssl dgst -sha512 -hex ${my_package} | awk '{print \$2}'", returnStdout: true).trim()
//                    def sha512Sum = sh(script: "shasum -a 512 ${env.app_package} | awk '{print \$1}'", returnStdout: true).trim()
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
