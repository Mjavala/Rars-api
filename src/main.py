import eventlet
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit

__version__ = "0.1.0"


def create_app():
    app = Flask(__name__)
    eventlet.monkey_patch()
    socketio = SocketIO(app, async_mode="eventlet")

    @app.route("/get_slide", methods=["POST"])
    def get_slide():
        # implement SCARA / Gantry movement logic
        # implement database communicaton
        """
        Returns: {
            'slide_id': String,
            'accepted': Bool,
            'slide_location': String,
            'box_location': String,
            'status': String (robot movement initiated, task scheduled, etc)
            'timestamp': Number (unix)
        }
        """
        data = request.get_json()
        return jsonify(
            {
                "slide_id": data["slide_id"],
                "accepted": True,
                "slide_location": "box_1_20",  # 20th slot in box 1
                "box_location": "conv_1_1",  # storage row 1 col 1
                "status": "Task schedule succesful",
                "timestamp": 1624012668,
            }
        )

    @app.route("/get_slides", methods=["POST"])
    def get_slides():
        # implement SCARA / Gantry movement logic
        # implement database communicaton
        """
        Returns: {
            'slide_ids': Array,
            'accepted': BOOL,
            'slide_location': String,
            'box_location': String,
            'status': String (robot movement initiated, task scheduled, etc)
            'timestamp': Number (unix)
        }
        """
        data = request.get_json()
        return jsonify(
            {
                "slide_ids": data["slide_ids"],
                "accepted": True,
                "status": "Task schedule succesful",
                "timestamp": 1624012668,
            }
        )

    @app.route("/store_slide", methods=["POST"])
    def store_slide():
        # implement SCARA / Gantry movement logic
        # implement database communicaton
        """
        Returns: {
            'slide_id': String,
            'accepted': Bool,
            'status': String (robot movement initiated, task scheduled, etc)
            'timestamp': Number (unix)
        }
        """
        data = request.get_json()
        return jsonify(
            {
                "slide_id": data["slide_id"],
                "accepted": False,
                "status": "Task schedule succesful",
                "timestamp": 1624012668,
            }
        )

    @app.route("/store_slides", methods=["POST"])
    def store_slides():
        # implement SCARA / Gantry movement logic
        # implement database communicaton
        """
        Returns: {
            'slide_ids': Array,
            'accepted': Bool,
            'status': String (robot movement initiated, task scheduled, etc)
            'timestamp': Number (unix)
        }
        """
        # data = request.get_json()
        return jsonify(
            {
                "slide_ids": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"],
                "accepted": False,
                "status": "Task schedule succesful",
                "timestamp": 1624012668,
            }
        )

    @socketio.on("connect")
    def on_connect():
        emit("Succesfully Connected to Server")

    @socketio.on("ping")
    def on_ping():
        emit("pong")

    @socketio.on_error_default
    def default_error_handler(e):
        print("Error in websockets: {0}".format(request))

    return app, socketio


if __name__ == "__main__":
    app, socketio = create_app()
    socketio.run(app, debug=True)
