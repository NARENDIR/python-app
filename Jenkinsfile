pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    sh "python${PYTHON_VERSION} -m venv ${VENV_DIR}"
                    sh "source ${VENV_DIR}/bin/activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh "source ${VENV_DIR}/bin/activate && pytest calculator/"
                }
            }
        }

        stage('Deploy Faulty Version') {
            steps {
                script {
                    // Intentionally introduce a fault
                    sh 'echo "Faulty Version" > application_version.txt'
                    // Deploy the faulty version 
                    sh './deploy.sh'
                }
            }
        }

        stage('Rollback') {
            steps {
                script {
                    // Run the rollback script
                    sh './rollback.sh'
                }
            }
        }
    }

    post {
        always {
            script {
                sh "deactivate || true"
            }
        }

        success {
            // Additional actions if the build is successful
        }

        failure {
            // Actions to be taken if the build fails
            script {
                unstable('Rolling back due to deployment failure') {
                    build job: 'python'
                }
            }
        }
    }
}

