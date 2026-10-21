
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test HTML Form') {
            steps {
                bat 'py -3 -m pip install pytest'
                bat 'py -3 -m pytest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'All HTML form tests passed!'
        }
        failure {
            echo 'HTML form tests failed. Check Console Output.'
        }
    }
}
