from src.main import create_app


def test_socket():
    app, socket = create_app()
    flask_test_client = app.test_client()
    socket_test_client = socket.test_client(
        app, flask_test_client=flask_test_client
    )

    # webserver connection test
    assert socket_test_client.is_connected()

    # connection event test
    socket_test_client.send("connect")
    received = socket_test_client.get_received()
    assert received[0]["name"] == "Succesfully Connected to Server"

    # test custom event
    socket_test_client.emit("ping")
    received = socket_test_client.get_received()
    assert received[0]["name"] == "pong"

    # test disconnect event
    disconnected = None
    status = socket_test_client.disconnect()
    assert disconnected == status
