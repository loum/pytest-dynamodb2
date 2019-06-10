"""Docker DynamoDB2 fixtures.

"""
import os
import boto3
import pytest
from lovely.pytest.docker.compose import Services


@pytest.fixture(scope='session')
def dynamodb_docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    """
    dirname = os.path.dirname(__file__)
    return [
        os.path.join(dirname,
                     'pytest_dynamodb2',
                     'docker',
                     'docker-compose.yml'),
    ]


@pytest.fixture(scope='session')
def dynamodb_docker_services(request,
                             pytestconfig,
                             dynamodb_docker_compose_files,
                             docker_ip):
    """Provide the docker services as a pytest fixture.

    The services will be stopped after all tests are run.
    """
    keep_alive = request.config.getoption("--keepalive", False)
    project_name = "pytest{}".format(str(pytestconfig.rootdir))
    services = Services(dynamodb_docker_compose_files,
                        docker_ip,
                        project_name)
    yield services
    if not keep_alive:
        services.shutdown()


@pytest.fixture(scope='session')
def dynamodb2_client(dynamodb_docker_services):
    dynamodb_docker_services.start('dynamodb2')
    dynamodb_docker_services.wait_for_service('dynamodb2', 8000)

    client = boto3.client('dynamodb',
                          endpoint_url='http://localhost:8000')

    return client
