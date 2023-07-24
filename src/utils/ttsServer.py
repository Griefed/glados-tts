import sys

from flask import send_file


class TTSServer:
    def __init__(self, engine, host="0.0.0.0", port=8124):  # 127.0.0.1
        self.engine = engine
        self.port = port
        self.host = host

    def start(self):
        from flask import Flask, request
        from flask_cors import CORS

        app = Flask(__name__)
        CORS(app)

        @app.route('/generate', methods=['POST'])
        def generate():
            text = request.form['text']
            result = self.engine.generate(text)
            return send_file(result.asMemoryFile(), mimetype='audio/wav', as_attachment=True, download_name='audio.wav')

        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None
        app.run(host=self.host, port=self.port)

# engine = TTSEngine.TTSEngine()
# engine.warmup()

# while(1):
#     result = engine.generate("Hello World you are a nice person")
#     result.save("test.wav")
#     tools.playAudio("test.wav")
#     os.unlink("test.wav")

#     result = engine.generate("You are also quite intelligent")
#     result.save("test.wav")
#     tools.playAudio("test.wav")
#     os.unlink("test.wav")
