pipeline {
    agent { label 'agent-1' }

    stages {
        stage('Code') {
            steps {
                echo 'Cloning GitHub Repository'
                git url: 'https://github.com/iammanishjangra/flask-sample-project.git',
                branch: 'main'
            }
        }

        stage('Dependencies') {
            steps {
                echo "Install Dependencies"
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                 sh '''
                 . venv/bin/activate
                //  BUILD_ID=dontKillMe nohup python3 app.py > app.log 2>&1 &
                python3 app.py
                 '''
            }
        }
    }
}
