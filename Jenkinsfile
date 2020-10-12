node {
    stage('Checkout'){
        checkout scm
    }

    stage('Clean Up'){
        dir("${env.WORKSPACE}") {
            sh 'python ./netconf/python/clean.py'
        }
    }

    stage('Configure') {
        dir("${env.WORKSPACE}") {
            sh 'python ./netconf/python/configure.py'
        }
    }
    stage('Test') {
        try {
            dir("${env.WORKSPACE}") {
                sh 'python ./test/test.py'
                junit allowEmptyResults: true, testResults: '**/test-reports/*.xml'
            }
        }
        catch(all) {
            junit allowEmptyResults: true, testResults: '**/test-reports/*.xml'
            sh "exit 1"
        }
    }
    stage('Publish Final') {
        dir("${env.WORKSPACE}") {
            sh 'python ./netconf/python/get_config.py > finalConfig.xml'
            archiveArtifacts artifacts: 'finalConfig.xml'
        }
    }
}