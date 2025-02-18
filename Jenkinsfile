stage('Checkout Code') {
    steps {
        git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/Xclusivep/myproject.git'
    }
}
stage('Build Docker Image') {
    steps {
        sh 'docker build -t xclusive001/fruit-app:$BUILD_NUMBER .'
    }
}
