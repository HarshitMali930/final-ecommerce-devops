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
                echo 'Checking Python syntax'
                sh 'python3 -m py_compile application/app/app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Installing dependencies and running tests'
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r application/requirements.txt
                    .venv/bin/python -m pip install pytest==9.0.3
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

        stage('Trivy Security Scan') {
            steps {
                echo 'Scanning Docker image for HIGH and CRITICAL vulnerabilities'
                sh '''
                    mkdir -p reports
                    trivy image \
                        --severity HIGH,CRITICAL \
                        --format json \
                        --output reports/trivy-jenkins-report.json \
                        final-ecommerce:latest
                '''
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
