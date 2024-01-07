rsync -e ssh -av \
  --exclude-from=.syncignore --progress \
  ./ root@127.0.0.1:/root/project/python-api-template
