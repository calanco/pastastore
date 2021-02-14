import pastastore

if __name__ == '__main__':
    app = pastastore.create_app(__name__)
    app.run()