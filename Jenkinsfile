pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile application/app/app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pip install --user -r application/requirements.txt'
                sh 'python3 -m pytest application/tests/ -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t final-ecommerce:latest .'
            }
        }
    }
}
