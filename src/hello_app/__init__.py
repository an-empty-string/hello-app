from flask import Flask, render_template, redirect, url_for

import collections
import datetime
import random
import socket
import subprocess
import threading

app = Flask(__name__)


load = threading.Event()
results = collections.deque()


def load_thread():
    while True:
        load.wait()

        number = random.randint(2**20, 2**24)
        original = number
        count = 0

        while load.is_set():
            if number == 1:
                if len(results) > 10:
                    results.pop()

                results.appendleft(f"{original} takes {count} iterations to fall to 1.")
                break

            elif number % 2 == 0:
                number /= 2
            else:
                number *= 3
                number += 1

            count += 1


threading.Thread(target=load_thread).start()


@app.route("/")
def index():
    return render_template(
        "index.html",
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
        name=socket.gethostname(),
        load=load.is_set(),
        stats=subprocess.check_output(["uptime"], text=True),
        results=results,
    )


@app.route("/toggle_load/")
def toggle_load():
    if load.is_set():
        load.clear()
    else:
        load.set()

    return redirect(url_for(".index"))
