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

        stage('Execute Python Script') {
            steps {
                script {
                    sh '''
                    python3 ${workspace}/download.py
                '''
                }
            }
        }
    }
}
