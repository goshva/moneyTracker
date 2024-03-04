#!/usr/bin/bash
cd /var/www/bots/moneyTracker
git pull && ./git-auto -o -p && git push
