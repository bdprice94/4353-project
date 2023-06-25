#!/bin/bash

pg_ctl -D ./db_data stop

tmux new-session -d -s app
tmux send-keys -t app 'pg_ctl -D ./db_data -l logfile start' C-m

tmux split-window -t app:0.0 -h
tmux send-keys -t app:0.1 'cd ./backend/ && python main.py' C-m

tmux split-window -t app:0.1 -v
tmux send-keys -t app:0.2 'cd ./frontend && npm start' C-m

tmux attach-session -t app