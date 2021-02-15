import pastastore
import argparse


def parse_arguments() -> (int, bool):
    parser = argparse.ArgumentParser(description="Run PastaStore REST API")
    parser.add_argument("--port", dest="port", type=int, default=5000,
                        help="The port where PastaStore is exposed to")
    parser.add_argument("--debug", action='store_true',
                        help="Paramter to set PastaStore in debug mode")
    args = parser.parse_args()

    return args.port, args.debug


if __name__ == '__main__':
    port, debug = parse_arguments()

    app = pastastore.create_app(__name__)
    app.run(port=port, debug=debug)
