"""Shakeout the DynamockDB docker instance.

"""
def test_docker_dynamodb2(dynamodb2_client):
    """Test a pristine DynamoDB2 instance.
    """
    # List pristine DynamoDB2 tables.
    received = dynamodb2_client.list_tables()

    msg = 'Pristine DynamoDB2 instance should not have any tables loaded'
    assert received.get('TableNames') == [], msg
