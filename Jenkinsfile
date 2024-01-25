pipeline {
    agent any
    
    parameters {
        string(name: 'User', description: 'Enter name of User')
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Replace 'https://github.com/your-username/your-repo.git' with your Git repository URL
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/your-username/your-repo.git']]])
                }
            }
        }

        stage('Execute Python Script') {
            steps {
                script {
                    // Replace 'your-script.py' with the actual name of your Python script
                    sh "python your-script.py --user ${params.User}"
                }
            }
        }
    }
}
