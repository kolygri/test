import unittest
from unittest.mock import MagicMock
import json
from redis_service import publish_message

class TestPublishMessage(unittest.TestCase):
    def test_publish_message_success(self):
        mock_redis = MagicMock()
        mock_redis.publish = MagicMock()

        with unittest.mock.patch('redis_service.r', mock_redis):
            publish_message('test_channel', {'key': 'value'})

            mock_redis.publish.assert_called_with('test_channel', json.dumps({'key': 'value'}))

    def test_publish_message_error(self):
        mock_redis = MagicMock()
        mock_redis.publish.side_effect = Exception("Test exception")

        with unittest.mock.patch('redis_service.r', mock_redis):
            with self.assertLogs() as log:
                publish_message('test_channel', {'key': 'value'})

                self.assertIn("Error publishing message to Redis: Test exception", log.output[0])
