import argparse
import os
from app import create_app


def parse_arguments() -> (int, bool, str):
    parser = argparse.ArgumentParser(description="Run PastaStore REST API")
    parser.add_argument("--port", dest="port", type=int, default=5000,
                        help="The port where PastaStore is exposed to")
    parser.add_argument("--debug", action='store_true',
                        help="Run PastaStore in debug mode")
    parser.add_argument("--env", dest="env", type=str, default="production",
                        choices=["development", "production"],
                        help="Set the Flask env")
    args = parser.parse_args()

    return args.port, args.debug, args.env


if __name__ == '__main__':
    port, debug, env = parse_arguments()

    os.environ['FLASK_ENV'] = env

    app = create_app(__name__)
    app.run(port=port, debug=debug)
