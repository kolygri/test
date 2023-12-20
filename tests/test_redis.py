from unittest.mock import MagicMock, patch
import json
from app.services.redis_service import (
    publish_message,
    set_key_value,
    get_key_value,
    push_to_list,
    get_from_list,
    set_key_with_expiration,
)


def test_publish_message_success():
    mock_redis = MagicMock()
    mock_redis.publish = MagicMock()

    with patch("app.services.redis_service.r", mock_redis):
        publish_message("test_channel", {"key": "value"})
        mock_redis.publish.assert_called_with("test_channel", json.dumps({"key": "value"}))


def test_publish_message_error(caplog):
    mock_redis = MagicMock()
    mock_redis.publish.side_effect = Exception("Test exception")

    with patch("app.services.redis_service.r", mock_redis):
        publish_message("test_channel", {"key": "value"})

        assert "Error publishing message to Redis: Test exception" in caplog.text


@patch("app.services.redis_service.r")
def test_set_key_value(mock_redis):
    set_key_value("test_key", {"foo": "bar"})
    mock_redis.set.assert_called_with("test_key", json.dumps({"foo": "bar"}))


@patch("app.services.redis_service.r")
def test_get_key_value(mock_redis):
    mock_redis.get.return_value = json.dumps({"foo": "bar"})
    result = get_key_value("test_key")
    assert result == {"foo": "bar"}


@patch("app.services.redis_service.r")
def test_push_to_list(mock_redis):
    push_to_list("test_list", {"foo": "bar"})
    mock_redis.lpush.assert_called_with("test_list", json.dumps({"foo": "bar"}))


@patch("app.services.redis_service.r")
def test_get_from_list(mock_redis):
    mock_redis.lrange.return_value = [json.dumps({"foo": "bar"})]
    result = get_from_list("test_list")
    assert result == [{"foo": "bar"}]


@patch("app.services.redis_service.r")
def test_set_key_with_expiration(mock_redis):
    set_key_with_expiration("test_key", {"foo": "bar"}, 60)
    mock_redis.setex.assert_called_with("test_key", 60, json.dumps({"foo": "bar"}))
