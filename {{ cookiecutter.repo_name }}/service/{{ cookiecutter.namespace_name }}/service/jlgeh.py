"""Json log global exception handler.

When gunicorn applications throw an exception early in start up running on k8s
logs can provide little to no diagnostic information.
"""


def write_log(*, message, tb_info=None):
    """Format message as json."""
    import json
    output = {
        "message": message,
        "exception": traceback.format_exc(),
        "levelname": "CRITICAL",
        "name": __name__,
        "pathname": __file__,
    }
    if tb_info is not None:
        output["exception"] = tb_info
    print(json.dumps(output), flush=True)


# Catch exceptions during startup.
try:
    from .app import app
except Exception as exp:
    import traceback
    write_log(message=str(exp), tb_info=str(traceback.format_exc()))
    raise RuntimeError from exp


if __name__ == "__main__":
    # Catch exceptions during serving.
    try:
        app.run()
    except Exception as exp:
        import traceback
        write_log(message=str(exp), tb_info=str(traceback.format_exc()))
        raise RuntimeError from exp
