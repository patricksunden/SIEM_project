
#!/usr/bin/env bash

USER="wronguser"
HOST="127.0.0.1"
PASS="wrongpassword"

# do 2 connections to trigger 3 password prompts each
for i in $(seq 1 6);
do
    echo "Attempt $i..."
    # Force password auth and disable keys, set prompt count
    sshpass -p "$PASS" ssh -o PreferredAuthentications=password \
        -o PubkeyAuthentication=no -o NumberOfPasswordPrompts=3 \
        -o StrictHostKeyChecking=no "$USER@$HOST" true
done
     
