
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application syntax'
                sh 'python3 -m py_compile application/app/app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Creating Python virtual environment and running tests'
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r application/requirements.txt
                    .venv/bin/python -m pytest application/tests/ -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t final-ecommerce:latest .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}

