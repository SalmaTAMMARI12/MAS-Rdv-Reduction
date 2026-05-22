from flask import Flask, Response, jsonify
import subprocess, sys, os, threading, queue

app = Flask(__name__, static_folder='.', static_url_path='')

log_queue = queue.Queue()
process_running = False

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/run', methods=['POST'])
def run_agents():
    global process_running
    if process_running:
        return jsonify({'error': 'Déjà en cours'}), 400
    process_running = True
    while not log_queue.empty():
        log_queue.get()
    def run():
        global process_running
        try:
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            proc = subprocess.Popen(
                [sys.executable, '-u', 'main.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace',
                bufsize=1,
                env=env,
                cwd=os.path.dirname(os.path.abspath(__file__))
            )
            for line in proc.stdout:
                log_queue.put(line.rstrip())
            proc.wait()
        finally:
            log_queue.put('__DONE__')
            process_running = False
    threading.Thread(target=run, daemon=True).start()
    return jsonify({'status': 'started'})

@app.route('/stream')
def stream():
    def generate():
        while True:
            try:
                line = log_queue.get(timeout=30)
                if line == '__DONE__':
                    yield f"data: __DONE__\n\n"
                    break
                yield f"data: {line}\n\n"
            except queue.Empty:
                yield f"data: ping\n\n"
    return Response(generate(), mimetype='text/event-stream',
                    headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'})

if __name__ == '__main__':
    app.run(debug=False, port=5000, threaded=True)