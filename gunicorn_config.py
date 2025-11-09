# Gunicorn config variables
loglevel = "warn"
errorlog = "-"  # stderr
worker_tmp_dir = "/dev/shm"
graceful_timeout = 120
timeout = 120
keepalive = 5
threads = 3
