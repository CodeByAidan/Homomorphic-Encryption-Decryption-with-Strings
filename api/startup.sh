#!/bin/bash

# Start the server script in the background
python server.py &

# Wait for a couple of seconds
sleep 2

# Run the client script
python client.py
