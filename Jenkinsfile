pipeline {
    agent any
    
    environment {
        DOCKER_CLI_PATH = "/usr/bin/docker"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/Xclusivep/myproject.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker version'  // Check if Jenkins can use Docker
                    sh 'docker build -t xclusive001/fruit-app:$BUILD_NUMBER .'
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker push xclusive001/fruit-app:$BUILD_NUMBER'
                }
            }
        }
    }
}
